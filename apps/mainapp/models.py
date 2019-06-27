# -*- coding: utf-8 -*-

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


class YGGoods(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='商品分类')  # 一级分类
    child_name = models.CharField(max_length=50, verbose_name='分类详情')
    name = models.CharField(max_length=50, verbose_name='商品名称')  # 商品名
    detail_name = models.CharField(max_length=100, verbose_name='商品描述', null=True)  # 商品描述
    price = models.FloatField(verbose_name='商品价格')  # 实际价格
    marketprice = models.FloatField(verbose_name='市场价格')  # 市场价
    goods_wheel_img = models.CharField(max_length=5000, verbose_name='商品图片')  # 轮播图  img[0] 对应的是 》小类id '40001:苹果'
    pro_addr = models.CharField(max_length=200, verbose_name='生产地')
    detail_img_url = models.CharField(max_length=5000, verbose_name='详情页图片')  # 详情页图片   'url#url#url'
    sale = models.IntegerField(verbose_name='销量')  # 销量
    stock = models.IntegerField(verbose_name='库存')  # 库存
    category_id = models.IntegerField(verbose_name='详情id')  # 销量
    child_id = models.IntegerField(verbose_name='分类id')  # 销量

    class Meta:
        db_table = 'goods'
        verbose_name = '商品表'
        verbose_name_plural = verbose_name


class YGUser(models.Model):
    GENDER_CHOICE = (
        (u'0', u'男'),
        (u'1', u'女'),
    )
    u_phone = models.CharField(max_length=30, verbose_name='手机号码')
    nickname = models.CharField(max_length=20, verbose_name='昵称', null=True)  # 昵称
    gender = models.CharField(choices=GENDER_CHOICE, verbose_name='性别',max_length=10,default=0)
    u_auth_string = models.CharField(max_length=256, verbose_name='用户密码')
    idcard = models.CharField(max_length=20, verbose_name='身份证', null=True)  # 身份证
    img = models.ImageField(verbose_name='用户头像',upload_to='img/%Y/%m/%d')  # 用户图像
    balance = models.FloatField(verbose_name='账户余额', default=0.00)
    level = models.CharField(max_length=20, verbose_name='用户等级', default='普通会员')

    class Meta:
        db_table = 'users'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name



class YGAddress(models.Model):
    user = models.ForeignKey(YGUser, on_delete=models.CASCADE, verbose_name='用户ID')
    address = models.CharField(max_length=500, verbose_name='用户地址')

    class Meta:
        db_table = 'address'
        verbose_name = '用户地址'
        verbose_name_plural = verbose_name


class YGCart(models.Model):
    c_user = models.ForeignKey(YGUser, on_delete=models.CASCADE,verbose_name='用户ID')
    c_goods = models.ForeignKey(YGGoods, on_delete=models.CASCADE,verbose_name='商品ID')
    c_goods_num = models.IntegerField(default=1,verbose_name='商品数量')
    c_is_select = models.BooleanField(default=True,verbose_name='是否选中')  # 是否选中，默认为选中

    class Meta:
        db_table = 'cart'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name


# ORDER_STATUS
# # 已下单未付款
# ORDER_STATUS_NOT_PAY = 0
# # 已下单已付款未发货
# ORDER_STATUS_NOT_SEND = 1
# # 已下单已付款已发货未收货
# ORDER_STATUS_NOT_RECEIVE = 2
# # 已下单已付款已发货已收货未确认
# ORDER_STATUS_NOT_AFFIRM = 3
# # 已下单已付款已发货已收货已确认未评价
# ORDER_STATUS_NOT_EVALUATE = 4
# # 已下单已付款已发货已收货已确认已评价未追评
# ORDER_STATUS_NOT_REVIEW = 5
# # 已下单已付款已发货已收货已确认已评价
# ORDER_STATUS_ORDER_STATUS_COMPLETE= 6


class YGOrder(models.Model):
    ORDER_STATUS = ((0, '已下单未付款'),
                    (1, '已下单已付款待收货'),
                    (2, '下单后待评论'))
    # (3,'已下单已付款已发货已收货未确认'),
    # (4,'已下单已付款已发货已收货已确认未评价'),
    # (5,'已下单已付款已发货已收货已确认已评价未追评'),
    # (6,'已下单已付款已发货已收货已确认已评价'),)
    o_user = models.ForeignKey(YGUser, on_delete=models.CASCADE, verbose_name='用户ID')
    o_price = models.FloatField(verbose_name='总价格')
    o_time = models.DateTimeField(auto_now=True, verbose_name='下单时间')
    o_status = models.IntegerField(choices=ORDER_STATUS,default=ORDER_STATUS[0], verbose_name='订单状态')

    class Meta:
        db_table = 'ygorders'
        verbose_name = '订单'
        verbose_name_plural = verbose_name


class YGOderDetail(models.Model):
    o_order = models.ForeignKey(YGOrder, on_delete=models.CASCADE,verbose_name='订单ID')
    o_goods = models.ForeignKey(YGGoods, on_delete=models.CASCADE,verbose_name='商品ID')
    o_goods_num = models.IntegerField(default=1,verbose_name='商品数量')

    class Meta:
        db_table = 'ygorderdetail'
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name


class YGComment(models.Model):
    user = models.ForeignKey(YGUser, on_delete=models.CASCADE, verbose_name='用户ID')
    order_id = models.ForeignKey(YGOrder, on_delete=models.CASCADE, verbose_name='订单ID')
    comments = models.CharField(max_length=500,verbose_name='用户评论')

    class Meta:
        db_table = 'comments'
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name


class YGEat(models.Model):
    eat_img = models.CharField(max_length=256, verbose_name='图片')
    eat_content = models.CharField(max_length=200, verbose_name='描述')
    eat_time = models.CharField(max_length=50, verbose_name='时间')

    class Meta:
        db_table = 'ygeat'
        verbose_name = '吃喝玩乐'
        verbose_name_plural = verbose_name




