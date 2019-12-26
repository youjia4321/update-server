from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Label(models.Model):
    name = models.CharField(verbose_name='类别', max_length=30)

    class Meta:
        db_table = 'user_label'
        verbose_name = '事务类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserProfile(AbstractUser):
    mobile = models.CharField(max_length=20, null=True, blank=True, verbose_name='联系方式')
    tag = models.ManyToManyField(Label, verbose_name='标签', default='')  # (多对多）

    class Meta:
        db_table = 'user_profile'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
