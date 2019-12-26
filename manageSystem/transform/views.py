from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
import json
from datetime import datetime
import os
# Create your views here.


# 处理温度
def is_write_temp(resp):
    # 获得当前时间
    now = datetime.now()
    # 转换为指定的格式
    otherStyleTime = now.strftime('%Y-%m-%d %H:%M:%S')
    dir_path = 'transform/no_temp/%s-TEMP.txt' % now.strftime('%Y-%m-%d')

    try:
        with open(dir_path, 'r', encoding='utf-8') as ff:
            data = ff.read()
    except FileNotFoundError:
        file = open(dir_path, 'w')
        print("文件创建成功！")
        with open(dir_path, 'r', encoding='utf-8') as ff:
            data = ff.read()

    if data == '':
        with open(dir_path, 'w', encoding='utf-8') as fp:
            results = {
                'timeline': [
                    str(otherStyleTime).split(" ")[1]
                ],
                'templine': [
                    resp['TEMP']
                ]
            }
            fp.write(json.dumps(results))
    else:
        _data = json.loads(data)
        _data['timeline'].append(str(otherStyleTime).split(" ")[1])
        _data['templine'].append(resp['TEMP'])
        with open(dir_path, 'w', encoding='utf-8') as fp:
            fp.write(json.dumps(_data))


is_start = False


def index(request):
    if request.method == 'GET':
        return HttpResponse('你好！')

    if request.method == 'POST':
        global is_start
        response = json.loads(str(request.body, 'utf-8'))
        for item in response:
            if item == 'TEMP':
                is_write_temp(response)

            if item == 'M0START':
                print('开始标液1浓度校准...，稀释浓度%s' % response[item])

            if item == 'M1START':
                print('开始标液2浓度校准...，稀释浓度%s' % response[item])

            if item == 'M2START':
                print('开始标液3浓度校准...，稀释浓度%s' % response[item])

            if item == 'MSSTART':
                is_start = True
                print('开始测量...，稀释浓度%s' % response[item])

        return JsonResponse({'code':'200', 'data': response})


def response_temp(request):
    now = datetime.now()
    dir_path = 'transform/no_temp/%s-TEMP.txt' % now.strftime('%Y-%m-%d')
    try:
        with open(dir_path, 'r', encoding='utf-8') as fp:
            data = json.loads(fp.read())
    
        result = {
            'code': '200',
            'times': data['timeline'],
            'temp': data['templine']
        }
    except: 
        result = {
            'code': '10001'
        }
    return JsonResponse({'data': result})