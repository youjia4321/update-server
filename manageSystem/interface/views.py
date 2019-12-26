from django.shortcuts import render
from django.views.generic.base import View
from interface.models import DocumentDownload, LogInfo
from equipments.models import Equipment, DocumentTag, SingleEquipmentDownload
from django.http import StreamingHttpResponse, HttpResponse, JsonResponse
import os
import json
from django.conf import settings
from django.utils.encoding import escape_uri_path  # 解决文件名包含中文
# Create your views here.


def index(request, *arg):
    return render(request, 'index.html')


def file_iterator(filename, chunk_size=512):
    with open(filename, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break


# 下载文件
def download_file_text(request, file_name):
    name = file_name.split('/')[-1]  # 显示在弹出对话框中的默认的下载文件名
    file_local = 'media/'+file_name  # 要下载的文件路径

    if not os.path.exists(file_local):
        return HttpResponse('File not found 404')

    response = StreamingHttpResponse(file_iterator(file_local))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Length'] = os.path.getsize(file_local)
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(escape_uri_path(name))
    return response


# 返回设备类型
def response_types(request):
    try:
        _types = DocumentTag.objects.all()
        _list = list()
        _type_list = list()
        if len(_types) != 0:
            for t in _types:
                _dic = dict()
                _type = dict()
                _dic['value'] = t.label
                _dic['label'] = t.label
                _type['type'] = t.label
                _list.append(_dic)
                _type_list.append(_type)
            data = {'code': '200', 'data': _list, 'type': _type_list}
            return JsonResponse({'result': data})
        error = dict()
        error['value'] = "暂无设备类型"
        error['label'] = "暂无设备类型"
        _list.append(error)
        data = {'code': '400', 'data': _list, 'type': _type_list}
        return JsonResponse({'result': data})
    except:
        data = {'code': '10001', 'msg': '服务器异常，稍后再试'}
        return JsonResponse({'result': data})


# 上传文件
def upload_files(request):
    file = request.FILES.get('file', '')
    _type = request.POST.get('type', '')
    path_dir = '%s/documents/%s' % (settings.MEDIA_ROOT, _type)
    is_exists = os.path.exists(path_dir)
    if not is_exists:
        os.makedirs(path_dir)
    file_addr = '%s/%s' % (path_dir, file.name)
    tag = DocumentTag.objects.get(label=_type)
    _doc = DocumentDownload.objects.filter(filename=file.name, tag=tag)
    if _doc:
        _version = _doc[0].version.split(".")
        _version[-1] = str(int(_version[-1]) + 1)
        version = ".".join(_version)
        single_docs = SingleEquipmentDownload.objects.filter(document_id=str(_doc[0].id), filename=file.name)
        for _single in single_docs:
            _single.delete()
        _doc[0].delete()
    else:
        version = "1.0.0"
    _document = 'documents/%s/%s' % (_type, file.name)
    record_document = DocumentDownload.objects.create(tag=tag, filename=file.name, document=_document, version=version)  # 储存数据
    equipments = tag.tag_equipments.all()
    if len(equipments) != 0:
        for _equip in equipments:
            SingleEquipmentDownload.objects.create(equipment=_equip, filename=file.name, document_id=str(record_document.id), document=_document, version=version)
    # 写入文件
    with open(file_addr, 'wb') as f:
        for f_img in file.chunks():
            f.write(f_img)
    data = {'code': '200', 'msg': '上传文件成功'}
    return JsonResponse({'result': data})


# combox响应
download = dict()


def check_equipment(equipment_tag=None, equipment_id=None):
    try:
        tag = DocumentTag.objects.get(label=equipment_tag)
        equipment = tag.tag_equipments.get(equipment_id=equipment_id)
        return equipment
    except:
        return None


def log_info(equipment_id, equipment_tag, error):
    msg = '设备ID：%s， 设备类型：%s，%s' % (equipment_id, equipment_tag, error)
    LogInfo.objects.create(info=msg)


def response_tf(equipment_id, equipment_tag, flag):
    resp = json.dumps({'DeviceID': equipment_id, 'DeviceType': equipment_tag, 'UPDATASTATUS': flag})
    return resp


class DownloadShowFile(View):
    def get(self, request):
        global download
        return HttpResponse(json.dumps(download), content_type="application/json")

    def post(self, request):
        global download
        download = {}
        equipment_id = request.POST.get('DeviceID', '')
        equipment_tag = request.POST.get('DeviceType', '')
        updata_status = request.POST.get('UPDATASTATUS', '')
        try:
            if updata_status == 'False':
                # if updata_status is False:
                download['url'] = "http://xxx.xxx.xxx.xxx:xxxx/download/"
                equipment = check_equipment(equipment_tag=equipment_tag, equipment_id=equipment_id)
                if equipment is not None:
                    if equipment.updated is True:
                        documents = equipment.single_equipment_documents.all()
                        for d in documents:
                            global_updated = DocumentDownload.objects.get(filename=d.filename)
                            if global_updated.updated is True:
                                if d.equipment.equipment_id == equipment_id:
                                    if d.equip_updated is True:
                                        download[d.filename] = str(d.document)
                                        d.equip_updated = False
                                        d.save()
                        if len(download) == 1:
                            log_info(equipment_id, equipment_tag, '暂无可更新文件')
                            return HttpResponse(response_tf(equipment_id, equipment_tag, False),
                                                content_type="application/json")
                        return HttpResponse(response_tf(equipment_id, equipment_tag, True),
                                            content_type="application/json")
                    else:
                        log_info(equipment_id, equipment_tag, '更新失败，设备禁止更新')
                        return HttpResponse(response_tf(equipment_id, equipment_tag, False),
                                            content_type="application/json")
                else:
                    log_info(equipment_id, equipment_tag, '更新失败，不存在此设备')
                    return HttpResponse(response_tf(equipment_id, equipment_tag, False),
                                        content_type="application/json")
            else:
                log_info(equipment_id, equipment_tag, '更新成功')
                return HttpResponse(response_tf(equipment_id, equipment_tag, True), content_type="application/json")
        except:
            log_info(equipment_id, equipment_tag, '更新失败，没接收到指定类型和序列号ID')
            return HttpResponse(
                json.dumps({'DeviceID': equipment_id, 'DeviceType': equipment_tag, 'UPDATASTATUS': False}),
                content_type="application/json")

