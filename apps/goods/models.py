from django.db import models

# Create your models here.
class YGGoods(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='商品分类')  # 一级分类
    child_name = models.CharField(max_length=50, verbose_name='分类详情')
    name = models.CharField(max_length=50, verbose_name='商品名称')  # 商品名
    detail_name = models.CharField(max_length=100, verbose_name='商品描述', null=True)  # 商品描述
    price = models.FloatField(verbose_name='商品价格')  # 实际价格
    marketprice = models.FloatField(verbose_name='市场价格')  # 市场价
    goods_wheel_img = models.CharField(max_length=5000, verbose_name='轮播图',
                                       null=True)  # 轮播图  img[0] 对应的是 》小类id '40001:苹果'
    pro_addr = models.CharField(max_length=200, verbose_name='生产地')
    detail_img_url = models.CharField(max_length=5000, verbose_name='详情页图片')  # 详情页图片   'url#url#url'
    sale = models.IntegerField(verbose_name='销量')  # 销量
    stock = models.IntegerField(verbose_name='库存')  # 库存
    category_id = models.IntegerField(verbose_name='详情id')  # 销量
    child_id = models.IntegerField(verbose_name='分类id')  # 销量
    goods_img = models.CharField(max_length=500, verbose_name='商品图片')
    is_chosen = models.BooleanField(verbose_name='是否精选', default=False)

    class Meta:
        db_table = 'goods'
        verbose_name = '商品表'
        verbose_name_plural = verbose_name

class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='一级分类')
    category_id = models.IntegerField(verbose_name='分类id')

    class Meta:
        db_table = 'category'
        verbose_name = '一级分类'
        verbose_name_plural = verbose_name


class Child(models.Model):
    child_name = models.CharField(max_length=50, verbose_name='二级分类')
    child_id = models.IntegerField(verbose_name='分类id')
    category_id = models.IntegerField(verbose_name='一级分类id')
    child_img = models.CharField(max_length=200,verbose_name='类图片')

    class Meta:
        db_table = 'child'
        verbose_name = '二级分类'
        verbose_name_plural = verbose_name