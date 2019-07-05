from django.db import models

class YGMain(models.Model):
    img = models.CharField(max_length=2000, verbose_name='图片')
    name = models.CharField(max_length=100, verbose_name='图片名称')
    trackid = models.IntegerField(verbose_name='图片ID')

    class Meta:
        abstract = True  # 抽象类

class YGWheel(YGMain):
    class Meta:
        db_table = 'wheel'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


class YGChosen(YGMain):
    class Meta:
        db_table = 'chosen'
        verbose_name = '精选推荐'
        verbose_name_plural = verbose_name


class YGNav(YGMain):
    class Meta:
        db_table = 'nav'
        verbose_name = '导航'
        verbose_name_plural = verbose_name


class YGNavDetail(YGMain):
    yg_productid = models.IntegerField()

    class Meta:
        db_table = 'details'
        verbose_name = '导航详情'
        verbose_name_plural = verbose_name


class Place(models.Model):  # 全国各大城市
    ISHOT = ((0, '非热门城市'), (1, '热门城市'))
    city_id = models.IntegerField(verbose_name='城市ID')
    nm = models.CharField(max_length=20, verbose_name='城市名称')
    ishot = models.IntegerField(choices=ISHOT, default=0, verbose_name='是否热门')
    py = models.CharField(max_length=50, verbose_name='拼音名称')

    class Meta:
        db_table = 'places'
        verbose_name = '全国各大城市'
        verbose_name_plural = verbose_name



