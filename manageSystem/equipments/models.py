from django.db import models
from interface.storage import OverwriteStorage
from datetime import datetime
# Create your models here.


class DocumentTag(models.Model):
    label = models.CharField(max_length=100, verbose_name="类型")

    class Meta:
        db_table = 'document_tag'
        verbose_name = "设备类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.label


class Equipment(models.Model):
    tag = models.ForeignKey(DocumentTag, related_name='tag_equipments', verbose_name='设备类型', on_delete=models.CASCADE,
                            null=True, blank=True)
    equipment_id = models.CharField(max_length=100, verbose_name='设备ID')
    updated = models.BooleanField(default=True, verbose_name="是否可更新设备")

    class Meta:
        db_table = 'equipment'
        verbose_name = '设备信息'
        unique_together = ('tag', 'equipment_id',)  # 联合唯一约束
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.equipment_id


class SingleEquipmentDownload(models.Model):
    equipment = models.ForeignKey(Equipment, related_name='single_equipment_documents', verbose_name='设备ID', on_delete=models.CASCADE, null=True, blank=True)
    filename = models.CharField(max_length=100, verbose_name='文件名称')
    document_id = models.CharField(max_length=100, verbose_name="文件ID", null=True, blank=True)
    document = models.FileField(upload_to='documents', default='', verbose_name='文件', storage=OverwriteStorage())
    version = models.CharField(max_length=50, default='1.0.0', verbose_name='版本号')
    equip_updated = models.BooleanField(default=True, verbose_name="根据设备可更新")
    # updated = models.BooleanField(default=True, verbose_name="全局可更新文件")
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        db_table = 'single_document_download'
        verbose_name = '单设备信息'
        unique_together = ('equipment', 'document_id',)
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.document)
