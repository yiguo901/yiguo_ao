from django.db import models

# Create your models here.
class YGEat(models.Model):
    eat_img = models.CharField(max_length=256, verbose_name='图片')
    eat_content = models.CharField(max_length=200, verbose_name='描述')
    eat_time = models.CharField(max_length=50, verbose_name='时间')

    class Meta:
        db_table = 'ygeat'
        verbose_name = '吃喝玩乐'
        verbose_name_plural = verbose_name