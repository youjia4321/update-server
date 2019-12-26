from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from users.models import UserProfile
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.


def check(username=None, password=None):
    try:
        user = UserProfile.objects.get(Q(username__exact=username) | Q(email__exact=username))
        # 用户可以用email和username进行登录，引用Q 相当于or
        if user.check_password(password):
            return user
        else:
            return False
    except Exception as e:
        return None


def user_login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = check(username=username, password=password)
    if user is not None:
        if user is not False:
            data = {'msg': 'Success!'}
            return JsonResponse({'data': data})
        else:
            data = {'msg': 'User password error'}
            return JsonResponse({'data': data})
    else:
        data = {'msg': 'User don\'t exist'}
        return JsonResponse({'data': data})


def user_logout(request):
    data = {'msg': 'Success!'}
    return JsonResponse({'data': data})


def modify_pwd(request):
    username = request.POST.get('user', '')
    new_pwd = request.POST.get('newPwd', '')
    user = UserProfile.objects.get(username=username)
    user.password = make_password(new_pwd)
    user.save()
    data = {'msg': 'Success!'}
    return JsonResponse({'data': data})


# 定义一个404方法，当输入的网址不存在时，则返回到404.html文件并在前端显示
def page_not_found(request):
    return render(request, '404.html')


# 定义一个500方法，当输入的网址不存在时，则返回到500.html文件并在前端显示
def page_error(request):
    return render(request, '500.html')
