import xadmin
from interface.models import DocumentDownload, LogInfo


class DocumentDownloadAdmin(object):
    """设置显示字段"""
    list_display = ["filename", "tag", "document", "updated", "add_time", "version"]
    search_fields = ["filename", "tag__label"]
    list_filter = ["filename", "version", "tag", "add_time", "updated"]
    list_editable = ["filename", "updated"]
    model_icon = "fa fa-folder-open"


class LogInfoAdmin(object):
    list_display = ['join_date', 'info']
    model_icon = "fa fa-cogs"


xadmin.site.register(DocumentDownload, DocumentDownloadAdmin)
xadmin.site.register(LogInfo, LogInfoAdmin)
