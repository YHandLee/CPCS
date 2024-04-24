from django.db import models


# Create your models here.


class Goods(models.Model):
    """商品表"""
    goods_img = models.CharField(verbose_name="图片链接", max_length=256)
    goods_title = models.CharField(verbose_name="商品标题", max_length=128)
    goods_price = models.DecimalField(verbose_name="商品价格", max_digits=10, decimal_places=3)
    goods_sales = models.CharField(verbose_name="商品销量", max_length=32)
    shop_title = models.CharField(verbose_name="店铺名", max_length=64)
    shop_platform = models.CharField(verbose_name="平台", max_length=32)
    goods_link = models.CharField(verbose_name="商品链接", max_length=128)
    grab_time = models.DateTimeField(verbose_name="抓取时间")
