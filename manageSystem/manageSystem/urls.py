"""manageSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import xadmin
from django.urls import path
from django.conf.urls import url, include
from django.views.static import serve
from django.conf import settings
from users.views import user_login, user_logout, modify_pwd
from interface.views import DownloadShowFile, download_file_text, upload_files, response_types, index
from equipments.views import create_tag, create_equipment, response_type_equipments,\
    response_table, response_single_table, delete_global_file, delete_global_files, \
    edit_global_file, edit_global_files, delete_single_file, delete_single_files, edit_single_file, edit_single_files, \
    delete_type, delete_equipment, response_equipment, delete_equipments, change_status


urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    # users app
    path('api/userLogin', user_login, name='userLogin'),
    path('api/userLogout', user_logout, name='userLogout'),
    path('api/modifyPassword', modify_pwd, name='modifyPassword'),

    url(r'^static/(?P<path>.*)/$', serve, {"document_root": settings.STATIC_ROOT}, name='static'),
    url(r'^media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}, name='media'),

    path('', index, name='index'),
    url(r'^system_(.*?)$', index, name='index'),
     # interface and equipments app

    path('download', DownloadShowFile.as_view(), name='download'),

   

    path('api/responseTypes', response_types, name='responseTypes'),
    path('api/createTag', create_tag, name='createTag'),
    path('api/createEquipInfo', create_equipment, name='createEquipInfo'),
    path('api/responseEquipments', response_type_equipments, name='responseEquipments'),
    path('api/responseSingleTable', response_single_table, name='responseSingleTable'),
    path('api/changeStatus', change_status, name='changeStatus'),
    path('api/responseTable', response_table, name='responseTable'),
    path('api/deleteGlobalFile', delete_global_file, name='deleteGlobalFile'),
    path('api/deleteGlobalFiles', delete_global_files, name='deleteGlobalFiles'),
    path('api/editGlobalFile', edit_global_file, name='editGlobalFile'),
    path('api/editGlobalFiles', edit_global_files, name='editGlobalFiles'),
    path('api/deleteSingleFile', delete_single_file, name='deleteSingleFile'),
    path('api/deleteSingleFiles', delete_single_files, name='deleteSingleFile'),
    path('api/editSingleFile', edit_single_file, name='editSingleFile'),
    path('api/editSingleFiles', edit_single_files, name='editSingleFiles'),
    path('api/deleteType', delete_type, name='deleteType'),  # add
    path('api/deleteEquipment', delete_equipment, name='deleteEquipment'),  # add
    path('api/deleteEquipments', delete_equipments, name='deleteEquipments'),  # add
    path('api/responseEquipment', response_equipment, name='responseEquipment'),  # add
    path('uploadFiles', upload_files, name='uploadFiles'),
    url(r'^download/(?P<file_name>.*)/$', download_file_text, name='download'),


    # transform app

    url(r'^transform/', include(('transform.urls', 'transform'), namespace='transform')),
]
