from lxml import etree
from time import sleep
from app01.utils.utils_func import draw_num, avoid_check
import time


def crawler(goods_word):
    goods_info = []
    bro = avoid_check()
    bro.get('https://suning.com/')
    # 标签定位
    search_input = bro.find_element('id', value='searchKeywords')
    # 搜索关键词
    search_input.send_keys(goods_word)
    # 点击搜索按钮
    btn = bro.find_element('id', value='searchSubmit')
    btn.submit()
    sleep(2)
    # 执行一组js程序滚动页面底部
    for i in range(1, 3):
        bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        sleep(3)
    # 数据解析
    tree = etree.HTML(bro.page_source)
    goods_li_list = (tree.xpath('//div[@id="product-list"]/ul/li'))
    # 最大页数
    max_page = ''.join(tree.xpath('//span[@class="page-more"]/text()'))
    #for i in range(1, int(draw_num(max_page))):
    for i in range(1, 3):
        # 点击下一页
        btn_next = bro.find_element('id', value='nextPage')
        url = btn_next.get_attribute('href')
        bro.get(url)
        sleep(2)
        # 执行一组js程序滚动页面底部
        for j in range(1, 3):
            bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(3)
        # 数据解析
        tree = etree.HTML(bro.page_source)
        goods_li_list = goods_li_list + (tree.xpath('//div[@id="product-list"]/ul/li'))
    i = 0
    for li in goods_li_list:
        # 图片
        goods_img = li.xpath('.//div[@class="img-block"]/a/img/@src')
        goods_img = 'https:' + goods_img[0]
        # 商品标题
        goods_title = ''.join(li.xpath('.//div[@class="title-selling-point"]/a//text()')).replace('\n', '')[0:127]
        # 商品价格
        goods_price = ''.join(li.xpath('.//div[@class="price-box"]/span/text()')).replace('\n', '') + \
                      ''.join(li.xpath('.//div[@class="price-box"]/span/i[2]/text()')).replace('\n', '')
        if draw_num(goods_price) == '':
            # goods_price = 0
            continue
        # 销量
        goods_sales = li.xpath('.//div[@class="info-evaluate"]/a/i/text()')
        if not goods_sales:
            goods_sales.append('未知')
        goods_sales = goods_sales[0]
        # 店铺名
        goods_shop = li.xpath('.//div[@class="store-stock"]/a/text()')
        if not goods_shop:
            goods_shop.append('未知')
        goods_shop = goods_shop[0]
        # 商品链接
        link_str = li.xpath('.//div[@class="title-selling-point"]/a/@sa-data')[0]
        link_list = link_str.split(',')
        link_shop_id = draw_num(link_list[2])
        link_prd_id = draw_num(link_list[1])
        goods_link = 'https://product.suning.com/' + link_shop_id + '/' + link_prd_id + '.html'
        # 平台
        goods_platform = '苏宁'
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

if __name__ == "__main__":
    word = "吹风机"
    sn_goods_info = crawler(goods_word=word)
    print(len(sn_goods_info), sn_goods_info)
