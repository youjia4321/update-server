import xadmin
from equipments.models import Equipment, DocumentTag, SingleEquipmentDownload

# Register your models here.


class EquipmentAdmin(object):
    list_display = ['updated', 'tag', 'equipment_id']
    list_filter = ['updated', 'tag', 'equipment_id']
    search_fields = ['equipment_id']
    list_editable = ["updated"]
    model_icon = "fa fa-desktop"


class DocumentTagAdmin(object):
    model_icon = "fa fa-info"


class SingleEquipmentDownloadAdmin(object):
    list_display = ["equipment", "filename", "document", "equip_updated", "add_time", "version"]
    search_fields = ["filename", "equipment__equipment_id"]
    list_filter = ["filename", "equipment", "equip_updated", "add_time"]
    list_editable = ["filename", "equip_updated"]
    model_icon = "fa fa-folder-open"


xadmin.site.register(DocumentTag, DocumentTagAdmin)
xadmin.site.register(Equipment, EquipmentAdmin)
xadmin.site.register(SingleEquipmentDownload, SingleEquipmentDownloadAdmin)
