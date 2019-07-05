from django.db import models

# Create your models here.
from user.helper import make_password



class YGUser(models.Model):
    level = (('0', '大众会员'), ('1', '白银会员'),
             ('2', '黄金会员'), ('3', '钻石会员'))
    sex = (('male', '男'), ('female', '女'))
    u_phone = models.CharField(max_length=30, verbose_name='手机号码', null=True)
    #    name = models.CharField(max_length=20, verbose_name='用户名')  # 用户名
    nickname = models.CharField(max_length=20, verbose_name='昵称', null=True)  # 昵称
    gender = models.CharField(max_length=10, verbose_name='性别', choices=sex, default='male',
                              null=True)  # 默认男 True  女是False
    u_auth_string = models.CharField(max_length=256, verbose_name='用户密码', null=True)
    idcard = models.CharField(max_length=20, verbose_name='身份证', null=True)  # 身份证
    img = models.ImageField(upload_to='img/%Y/%m/%d', verbose_name='用户图像', null=True, blank=True)  # 用户图像
    balance = models.FloatField(verbose_name='账户余额', default=0.0, null=True)
    u_level = models.CharField(max_length=20, choices=level, verbose_name='用户等级', default=0, null=True)
    is_active = models.BooleanField(verbose_name='是否激活', default=False)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    def __str__(self):
        return self.nickname

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if len(self.u_auth_string) < 32:
            self.u_auth_string = make_password(self.u_auth_string)
        super().save()

    class Meta:
        db_table = 'users'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

