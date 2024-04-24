from lxml import etree
from time import sleep
from app01.utils.utils_func import draw_num, avoid_check
import time


def crawler(goods_word):
    goods_info = []
    bro = avoid_check()
    bro.get('https://jd.com/')
    # 标签定位
    search_input = bro.find_element('id', value='key')
    # 搜索关键词
    search_input.send_keys(goods_word)
    # 点击搜索按钮
    btn = bro.find_element('class name', value='button')
    btn.click()
    sleep(2)
    # 执行一组js程序滚动页面置底
    bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(2)
    # 数据解析
    tree = etree.HTML(bro.page_source)
    goods_li_list = (tree.xpath('//div[@id="J_goodsList"]/ul/li'))
    # 最大页数
    max_page = tree.xpath('//span[@class="p-skip"]/em/b/text()')[0]
    #for i in range(1, int(max_page)):
    for i in range(1, 3):
        # 点击下一页
        btn_next = bro.find_element('class name', value='pn-next')
        btn_next.click()
        sleep(2)
        # 执行一组js程序滚动页面置底
        bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        sleep(2)
        # 数据解析
        tree = etree.HTML(bro.page_source)
        goods_li_list = goods_li_list + (tree.xpath('//div[@id="J_goodsList"]/ul/li'))
    i = 0
    for li in goods_li_list:
        # 图片
        goods_img = li.xpath('.//div[@class="p-img"]/a/img/@src')
        if not goods_img:
            goods_img = li.xpath('.//div[@class="p-img"]/a/img/@data-lazy-img')
        goods_img = 'https:' + goods_img[0]
        # 商品标题
        goods_title = ''.join(li.xpath('.//div[@class="p-name p-name-type-2"]/a/em//text()'))
        # 商品价格
        goods_price = li.xpath('.//div[@class="p-price"]/strong/i/text()')[0]
        if draw_num(goods_price) == '':
            goods_price = 0
        # 销量
        goods_sales = li.xpath('.//div[@class="p-commit"]/strong/a/text()')
        if not goods_sales:
            goods_sales.append('未知')
        goods_sales = goods_sales[0]
        # 店铺名
        goods_shop = li.xpath('.//div[@class="p-shop"]/span/a/@title')
        if not goods_shop:
            goods_shop.append('未知')
        goods_shop = goods_shop[0]
        # 商品链接
        goods_link = 'https:' + ''.join(li.xpath('.//div[@class="p-name p-name-type-2"]/a/@href'))
        # 平台
        goods_platform = '京东'
        i = i + 1
        goods_info.append({
            'goods_img': goods_img,
            'goods_title': goods_title,
            'goods_price': float(goods_price),
            'goods_sales': goods_sales,
            'shop_title': goods_shop,
            'shop_platform': goods_platform,
            'goods_link': goods_link,
            'grab_time': time.strftime('%Y-%m-%d %H:%M', time.localtime())
        })
    sleep(5)
    # 关闭无头浏览器
    bro.quit()
    return goods_info

