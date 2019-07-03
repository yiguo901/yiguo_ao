from django.db import models

from goods.models import YGGoods
from user.models import YGUser

# Create your models here.
class Base(models.Model):
    create_time = models.DateTimeField(verbose_name='注册时间',
                                       auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间',
                                       auto_now=True)

    class Meta:
        abstract = True  # 抽象类


class YGCart(Base):
    c_user = models.ForeignKey(YGUser, on_delete=models.CASCADE, verbose_name='用户ID')
    c_goods = models.ForeignKey(YGGoods, on_delete=models.CASCADE, verbose_name='商品ID')
    c_goods_num = models.IntegerField(default=1, verbose_name='商品数量')
    # goods_num = models.IntegerField(verbose_name='商品总件数')
    c_is_select = models.BooleanField(default=True, verbose_name='是否选中')  # 是否选中，默认为选中
    total_price = models.FloatField(verbose_name='总价格',default=0.00)

    class Meta:
        db_table = 'cart'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name


# ORDER_STATUS
# # 已下单未付款
# ORDER_STATUS_NOT_PAY = 0
# # 未发货
# ORDER_STATUS_NOT_SEND = 1
# # 确认收货且发表评论
# ORDER_STATUS_NOT_RECEIVE = 2



class YGOrder(Base):
    ORDER_STATUS = ((0, '已下单未付款'),
                    (1, '已下单已付款待收货'),
                    (2, '下单后待评论'))
    o_user = models.ForeignKey(YGUser, on_delete=models.CASCADE, verbose_name='用户ID')
    o_price = models.FloatField(verbose_name='总价格')
    o_time = models.DateTimeField(auto_now=True, verbose_name='下单时间')
    o_status = models.CharField(max_length=20, choices=ORDER_STATUS, default=0, verbose_name='订单状态')

    class Meta:
        db_table = 'orders'
        verbose_name = '订单'
        verbose_name_plural = verbose_name


class YGOderDetail(models.Model):
    o_order = models.ForeignKey(YGOrder, on_delete=models.CASCADE, verbose_name='订单ID')
    o_goods = models.ForeignKey(YGGoods, on_delete=models.CASCADE, verbose_name='商品ID')
    o_goods_num = models.IntegerField(default=1, verbose_name='商品数量')

    """
    地址，
    状态


    """

    class Meta:
        db_table = 'orderdetail'
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name


class YGComment(Base):
    user = models.ForeignKey(YGUser, on_delete=models.CASCADE, verbose_name='用户ID')
    order_id = models.ForeignKey(YGOrder, on_delete=models.CASCADE, verbose_name='订单ID')
    comments = models.CharField(max_length=500, verbose_name='用户评论')

    class Meta:
        db_table = 'comments'
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name



class YGAddress(Base):
    state = ((0, '公司地址'), (1, '家庭地址'))
    user_id = models.ForeignKey(YGUser, on_delete=models.CASCADE, verbose_name='用户ID')
    address = models.CharField(max_length=500, verbose_name='用户地址')
    addr_type = models.IntegerField(verbose_name='地址状态', choices=state, default=0)

    class Meta:
        db_table = 'address'
        verbose_name = '用户地址'
        verbose_name_plural = verbose_name


