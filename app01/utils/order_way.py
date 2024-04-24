
class OrderWay(object):
    def __init__(self, queryset):
        self.queryset = queryset

    def order(self, opt):
        if opt == 'pri_o':
            queryset = self.queryset.order_by("goods_price")
        elif opt == 'pri_d':
            queryset = self.queryset.order_by("-goods_price")
        elif opt == 'tim_o':
            queryset = self.queryset.order_by("grab_time")
        elif opt == 'tim_d':
            queryset = self.queryset.order_by("-grab_time")
        else:
            queryset = self.queryset.order_by("goods_title")
        return queryset
