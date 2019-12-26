from django.contrib import admin
from users.models import UserProfile, Label
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Label)
