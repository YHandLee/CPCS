from app01 import models
from app01.utils.bootstrap import BootStrapModelForm


class GoodsModelForm(BootStrapModelForm):

    class Meta:
        model = models.Goods
        fields = ["goods_img", "goods_title", "goods_price", "goods_sales", "shop_title",
                  "shop_platform", "goods_link", "grab_time"]