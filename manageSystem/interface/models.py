from django.db import models
from datetime import datetime
from equipments.models import Equipment, DocumentTag
from interface.storage import OverwriteStorage
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
import os
# Create your models here.


class DocumentDownload(models.Model):
    tag = models.ForeignKey(DocumentTag, related_name='tag_documents', verbose_name='文件类型', on_delete=models.CASCADE, null=True, blank=True)
    filename = models.CharField(max_length=100, verbose_name='文件名称')
    document = models.FileField(upload_to='documents', default='', verbose_name='文件', storage=OverwriteStorage())
    version = models.CharField(max_length=50, default='1.0.0', verbose_name='版本号')
    # equip_updated = models.BooleanField(default=True, verbose_name="根据设备可更新")
    updated = models.BooleanField(default=True, verbose_name="全局可更新文件")
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)
    # 多对一（文件--类别）
    '''
    一个文件类型下面的所有文件：
    tag.tag_documents.all()
    '''

    class Meta:
        db_table = 'document_download'
        unique_together = ('tag', 'filename',)  # 联合唯一约束
        verbose_name = '文件管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.document)


@receiver(pre_delete, sender=DocumentDownload)
def global_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.document.delete(False)  # False 表示model不保存

pre_delete.connect(global_delete, sender=DocumentDownload)


class LogInfo(models.Model):
    info = models.CharField(max_length=200, verbose_name="日志内容")
    join_date = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        db_table = 'document_log'
        verbose_name = '日志信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.join_date)
