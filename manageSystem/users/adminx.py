import xadmin
from xadmin import views
from users.models import UserProfile, Label

class BaseXadminSetting(object):
    enable_themes = True
    use_bootswatch = True


class CommXadminSetting(object):
    site_title = u'炜麒智能终端管理系统'
    site_footer = u'四川炜麒科技股份有限公司'
    # menu_style = 'accordion'


class LabelAdmin(object):
    model_icon = "fa fa-tags"


xadmin.site.register(Label, LabelAdmin)
xadmin.site.register(views.BaseAdminView, BaseXadminSetting)
xadmin.site.register(views.CommAdminView, CommXadminSetting)