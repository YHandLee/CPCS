from django.shortcuts import render
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.order_way import OrderWay


def product_list(request):
    data_dict = {}
    search_data = request.GET.get('query', '')
    if search_data:
        data_dict["goods_title__contains"] = search_data
        data_dict["goods_title__contains"] = search_data.upper()
    queryset = models.Goods.objects.filter(**data_dict)
    order_type = request.GET.get('opt', 'def')
    order_queryset = OrderWay(queryset).order(order_type)
    page_obj = Pagination(request, order_queryset, page_size=30)
    context = {
        "search_data": search_data,
        "order_type": order_type,
        "queryset": page_obj.page_queryset,
        "page_string": page_obj.html(),
    }
    return render(request, 'product_list.html', context)
