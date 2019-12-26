from django.contrib import admin
from interface.models import DocumentDownload, LogInfo
# Register your models here.


class DocumentDownloadAdmin(admin.ModelAdmin):
    list_display = ("filename","tag", "document", "version", "updated")


admin.site.register(DocumentDownload, DocumentDownloadAdmin)
admin.site.register(LogInfo)
