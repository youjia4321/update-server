from equipments.models import DocumentTag, Equipment, SingleEquipmentDownload
from interface.models import DocumentDownload, global_delete
from django.http import JsonResponse
import json

# Create your views here.


def create_tag(request):
    try:
        tag = request.POST.get('tag', '')
        _tag = DocumentTag.objects.filter(label=tag)
        if len(_tag) != 0:
            data = {'code': '10001', 'msg': '设备类型已存在'}
            return JsonResponse({'result': data})
        DocumentTag.objects.create(label=tag)
        data = {'code': '200'}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})


def create_equipment(request):
    try:
        tag = request.POST.get('tag', '')
        equipment_id = request.POST.get('equipment_id', '')
        _type = DocumentTag.objects.get(label=tag)
        _equip = Equipment.objects.filter(tag=_type, equipment_id=equipment_id)
        if len(_equip) != 0:
            data = {'code': '10001', 'msg': '设备信息已存在'}
            return JsonResponse({'result': data})
        equip = Equipment.objects.create(tag=_type, equipment_id=equipment_id)
        _type_documents = _type.tag_documents.all()
        for _doc in _type_documents:
            SingleEquipmentDownload.objects.create(equipment=equip, document_id=str(_doc.id), filename=_doc.filename, document=_doc.document,
                                                   version=_doc.version)
        data = {'code': '200'}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})


def response_type_equipments(request):
    try:
        tag = request.POST.get('tag', '')
        _type = DocumentTag.objects.get(label=tag)
        equipments = _type.tag_equipments.all()
        _list = list()
        if len(equipments) != 0:
            for e in equipments:
                _dic = dict()
                _dic['value'] = e.equipment_id
                _dic['label'] = e.equipment_id
                _list.append(_dic)
            data = {'code': '200', 'data': _list}
            return JsonResponse({'result': data})
        error = dict()
        error['value'] = "暂无设备信息"
        error['label'] = "暂无设备信息"
        _list.append(error)
        data = {'code': '400', 'msg': '此类型暂无设备信息', 'data': _list}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})


def response_table(request):
    try:
        tag = request.POST.get('tag', '')
        _type = DocumentTag.objects.get(label=tag)
        _equip_documents = _type.tag_documents.all().order_by("-add_time")
        doc_list = list()
        if len(_equip_documents) != 0:
            for doc in _equip_documents:
                doc_dict = dict()
                doc_dict['date'] = str(doc.add_time)
                doc_dict['filename'] = doc.filename
                doc_dict['updated'] = str(doc.updated)
                doc_dict['position'] = str(doc.document)
                doc_dict['version'] = doc.version
                doc_list.append(doc_dict)
            data = {'code': '200', 'data': doc_list}
            return JsonResponse({'result': data})
        data = {'code': '400', 'data': doc_list}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})


def response_single_table(request):
    try:
        tag = request.POST.get('tag', '')
        equipment_id = request.POST.get('equipment_id', '')
        _type = DocumentTag.objects.get(label=tag)
        single_equip = Equipment.objects.get(tag=_type, equipment_id=equipment_id)
        # print(single_equip.updated)

        _equip_documents = single_equip.single_equipment_documents.all().order_by("-add_time")
        doc_list = list()
        if len(_equip_documents) != 0:
            for doc in _equip_documents:
                doc_dict = dict()
                doc_dict['date'] = str(doc.add_time)
                doc_dict['filename'] = doc.filename
                doc_dict['updated'] = str(doc.equip_updated)
                doc_dict['position'] = str(doc.document)
                doc_dict['version'] = doc.version
                doc_list.append(doc_dict)
            data = {'code': '200', 'data': doc_list, 'is_update': str(single_equip.updated)}
            return JsonResponse({'result': data})
        data = {'code': '400', 'data': doc_list}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})


def change_status(request):
    try:
        tag = request.POST.get('tag', '')
        equipment_id = request.POST.get('equipment_id', '')
        # print(tag, equipment_id)
        _type = DocumentTag.objects.get(label=tag)
        single_equip = Equipment.objects.get(tag=_type, equipment_id=equipment_id)
        single_equip.updated = true2false(single_equip.updated)
        single_equip.save()
        data = {'code': '200', 'is_update': str(single_equip.updated)}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})


def delete_global_file(request):
    try:
        tag = request.POST.get('tag', '')
        filename = request.POST.get('filename', '')
        _type = DocumentTag.objects.get(label=tag)
        document = DocumentDownload.objects.get(tag=_type, filename=filename)
        single_equipment_documents = SingleEquipmentDownload.objects.filter(document_id=str(document.id), filename=filename)
        document.delete()  # 全局文件删除并且删除本地文件
        for _t in single_equipment_documents:
            _t.delete()  # 单设备文件删除 不删除本地文件
        data = {'code': '200'}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})


def delete_global_files(request):
    try:
        tag = request.POST.get('tag', '')
        file_list = request.POST.get('filelist', '')
        _type = DocumentTag.objects.get(label=tag)
        for file in json.loads(file_list):
            document = DocumentDownload.objects.get(tag=_type, filename=file['filename'])
            single_equipment_documents = SingleEquipmentDownload.objects.filter(document_id=str(document.id), filename=file['filename'])
            document.delete()  # 全局多文件删除
            for _t in single_equipment_documents:
                _t.delete()  # 单设备文件删除
        data = {'code': '200'}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})


def true2false(flag):
    if flag is True:
        flag = False
    else:
        flag = True
    return flag


def edit_global_file(request):
    try:
        tag = request.POST.get('tag', '')
        filename = request.POST.get('filename', '')
        _type = DocumentTag.objects.get(label=tag)
        document = DocumentDownload.objects.get(tag=_type, filename=filename)
        document.updated = true2false(document.updated)
        document.save()
        data = {'code': '200'}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})


def edit_global_files(request):
    try:
        post_data = json.loads(str(request.body, 'utf-8'))
        tag = post_data['tag']
        _type = DocumentTag.objects.get(label=tag)
        file_list = post_data['filelist']
        for file in file_list:
            document = DocumentDownload.objects.get(tag=_type, filename=file['filename'])
            document.updated = true2false(document.updated)
            document.save()
        data = {'code': '200'}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})


def delete_single_file(request):
    try:
        tag = request.POST.get('tag', '')
        equipment_id = request.POST.get('equipment_id', '')
        filename = request.POST.get('filename', '')
        _type = DocumentTag.objects.get(label=tag)
        single_equipment = Equipment.objects.get(tag=_type, equipment_id=equipment_id)
        single_document = SingleEquipmentDownload.objects.get(equipment=single_equipment, filename=filename)
        single_document.delete()
        data = {'code': '200'}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})


def delete_single_files(request):
    try:
        tag = request.POST.get('tag', '')
        equipment_id = request.POST.get('equipment_id', '')
        file_list = request.POST.get('filelist', '')
        _type = DocumentTag.objects.get(label=tag)
        single_equipment = Equipment.objects.get(tag=_type, equipment_id=equipment_id)
        for file in json.loads(file_list):
            single_document = SingleEquipmentDownload.objects.get(equipment=single_equipment, filename=file['filename'])
            single_document.delete()
        data = {'code': '200'}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})


def edit_single_file(request):
    try:
        tag = request.POST.get('tag', '')
        equipment_id = request.POST.get('equipment_id', '')
        filename = request.POST.get('filename', '')
        _type = DocumentTag.objects.get(label=tag)
        single_equipment = Equipment.objects.get(tag=_type, equipment_id=equipment_id)
        single_document = SingleEquipmentDownload.objects.get(equipment=single_equipment, filename=filename)
        single_document.equip_updated = true2false(single_document.equip_updated)
        single_document.save()
        data = {'code': '200'}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})


def edit_single_files(request):
    try:
        tag = request.POST.get('tag', '')
        equipment_id = request.POST.get('equipment_id', '')
        file_list = request.POST.get('filelist', '')
        _type = DocumentTag.objects.get(label=tag)
        single_equipment = Equipment.objects.get(tag=_type, equipment_id=equipment_id)
        for file in json.loads(file_list):
            single_document = SingleEquipmentDownload.objects.get(equipment=single_equipment, filename=file['filename'])
            single_document.equip_updated = true2false(single_document.equip_updated)
            single_document.save()
        data = {'code': '200'}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})


# add
def delete_type(request):
    try:
        tag = request.POST.get('tag', '')
        _type = DocumentTag.objects.get(label=tag)
        _type.delete()
        data = {'code': '200'}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})


def response_equipment(request):
    try:
        equipments = Equipment.objects.all()
        _list = list()
        if len(equipments) != 0:
            for e in equipments:
                _dic = dict()
                _dic['equip_id'] = e.equipment_id
                _list.append(_dic)
        data = {'code': '200', 'data': _list}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})


def delete_equipment(request):
    try:
        equipment_id = request.POST.get('equipment_id', '')
        equipment = Equipment.objects.get(equipment_id=equipment_id)
        equipment.delete()
        data = {'code': '200'}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})


def delete_equipments(request):
    try:
        equipments = request.POST.get('equipments', '')
        for e in json.loads(equipments):
            equip = Equipment.objects.get(equipment_id=e['equip_id'])
            equip.delete()
        data = {'code': '200'}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})
