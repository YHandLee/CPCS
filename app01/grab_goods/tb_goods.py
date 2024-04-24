from lxml import etree
from time import sleep
from selenium.webdriver.common.by import By
from app01.utils.utils_func import draw_num, avoid_check
import time


def crawler(goods_word):
    goods_info = []
    cookies = [
        {'domain': '.taobao.com', 'httpOnly': False, 'name': 'uc1', 'path': '/', 'sameSite': 'None', 'secure': True,
         'value': 'cookie21=UIHiLt3xSalX&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&pas=0&cookie15=WqG3DMC9VAQiUQ%3D%3D&cookie14=UoezRm%2BvPbCsLw%3D%3D&existShop=false'},
        {'domain': '.taobao.com', 'expiry': 1695460376, 'httpOnly': False, 'name': 'isg', 'path': '/',
         'sameSite': 'Lax', 'secure': False,
         'value': 'BLu7Q0OXW-PnTWdXw6sRQg2FSp8lEM8SkDXQ4K14l7rRDNvuNeBfYtnOIq1CLCcK'},
        {'domain': '.taobao.com', 'expiry': 1680513176, 'httpOnly': False, 'name': '_m_h5_tk_enc', 'path': '/',
         'sameSite': 'None', 'secure': True, 'value': '4dc6bb0c347828258a9941d96a66a10e'},
        {'domain': '.taobao.com', 'expiry': 1680513176, 'httpOnly': False, 'name': '_m_h5_tk', 'path': '/',
         'sameSite': 'None', 'secure': True, 'value': '3ce49236d185547a670bb4eb915b5803_1679917016844'},
        {'domain': '.taobao.com', 'expiry': 1711444376, 'httpOnly': False, 'name': 'thw', 'path': '/',
         'sameSite': 'Lax', 'secure': False, 'value': 'cn'},
        {'domain': '.taobao.com', 'httpOnly': False, 'name': 'dnk', 'path': '/', 'sameSite': 'None', 'secure': True,
         'value': 'tb919827938'},
        {'domain': '.taobao.com', 'httpOnly': False, 'name': 'cancelledSubSites', 'path': '/', 'sameSite': 'None',
         'secure': True, 'value': 'empty'},
        {'domain': '.taobao.com', 'httpOnly': True, 'name': 'cookie1', 'path': '/', 'sameSite': 'None', 'secure': True,
         'value': 'AibnVn%2FXE5nMPO9lB69K2Qtq9gb8s8t%2BS3%2Fwcx2jLeg%3D'},
        {'domain': '.taobao.com', 'httpOnly': False, 'name': '_l_g_', 'path': '/', 'sameSite': 'None', 'secure': True,
         'value': 'Ug%3D%3D'},
        {'domain': '.taobao.com', 'httpOnly': False, 'name': '_nk_', 'path': '/', 'sameSite': 'None', 'secure': True,
         'value': 'tb919827938'},
        {'domain': '.taobao.com', 'httpOnly': False, 'name': 'existShop', 'path': '/', 'sameSite': 'None',
         'secure': True, 'value': 'MTY3OTkwODM3NA%3D%3D'},
        {'domain': '.taobao.com', 'expiry': 1680541976, 'httpOnly': False, 'name': 'mt', 'path': '/',
         'sameSite': 'None', 'secure': True, 'value': 'ci=1_1'},
        {'domain': '.taobao.com', 'expiry': 1682529174, 'httpOnly': False, 'name': 'lgc', 'path': '/',
         'sameSite': 'None', 'secure': True, 'value': 'tb919827938'},
        {'domain': '.taobao.com', 'httpOnly': False, 'name': 'sg', 'path': '/', 'sameSite': 'None', 'secure': True,
         'value': '810'},
        {'domain': '.taobao.com', 'expiry': 1711473174, 'httpOnly': False, 'name': '_cc_', 'path': '/',
         'sameSite': 'None', 'secure': True, 'value': 'V32FPkk%2Fhw%3D%3D'},
        {'domain': '.taobao.com', 'httpOnly': True, 'name': 'cookie17', 'path': '/', 'sameSite': 'None', 'secure': True,
         'value': 'UUpgRSvYmXAFO2R21A%3D%3D'},
        {'domain': '.taobao.com', 'expiry': 1695460375, 'httpOnly': False, 'name': 'tfstk', 'path': '/',
         'sameSite': 'Lax', 'secure': False,
         'value': 'cNb5BNwOSYDSxpUnrLNVlkM4xaTdZWwXiu9RN8kU1VfnUd15iYgwC-YVxxYe9I1..'},
        {'domain': '.taobao.com', 'httpOnly': False, 'name': 'csg', 'path': '/', 'sameSite': 'None', 'secure': True,
         'value': 'e61a81d7'},
        {'domain': '.taobao.com', 'expiry': 1682529174, 'httpOnly': True, 'name': 'uc3', 'path': '/',
         'sameSite': 'None', 'secure': True,
         'value': 'lg2=UIHiLt3xD8xYTw%3D%3D&nk2=F5RMGL%2BDdWVJqo0%3D&vt3=F8dCsfT3KG9Ip%2FgLHlQ%3D&id2=UUpgRSvYmXAFO2R21A%3D%3D'},
        {'domain': '.taobao.com', 'httpOnly': True, 'name': 'unb', 'path': '/', 'sameSite': 'None', 'secure': True,
         'value': '2213345236741'},
        {'domain': '.taobao.com', 'expiry': 1687713174, 'httpOnly': False, 'name': 't', 'path': '/', 'sameSite': 'None',
         'secure': True, 'value': '22765a76e739a38de45cd3c71a50006f'},
        {'domain': '.taobao.com', 'httpOnly': True, 'name': 'skt', 'path': '/', 'sameSite': 'None', 'secure': True,
         'value': '5083e10040e70e7d'},
        {'domain': '.taobao.com', 'expiry': 1711473174, 'httpOnly': True, 'name': 'sgcookie', 'path': '/',
         'sameSite': 'None', 'secure': True,
         'value': 'E10001GgkujaA%2B76zud24b2q2tvczNuAhk96MebkWl7n%2F7C6D%2Fk0AJO%2BOTbiFD%2BwnXWKznKGoGJa5nnU0izcS4GBVYw2zWGyPS64kcAXhoT0YuU%3D'},
        {'domain': '.taobao.com', 'expiry': 1682529174, 'httpOnly': True, 'name': 'uc4', 'path': '/',
         'sameSite': 'None', 'secure': True,
         'value': 'nk4=0%40FY4HXZa59%2F%2BY50KIbqUl4Rwkgj9Abw%3D%3D&id4=0%40U2gqykM8qQlm1sGNQqNYziDzL%2FZ0lgc2'},
        {'domain': '.taobao.com', 'httpOnly': True, 'name': 'cookie2', 'path': '/', 'sameSite': 'None', 'secure': True,
         'value': '154b07d5d8828f37d06b4d81a769046a'},
        {'domain': '.taobao.com', 'expiry': 1695460375, 'httpOnly': False, 'name': 'l', 'path': '/', 'sameSite': 'Lax',
         'secure': False,
         'value': 'fBruQTsqNEwXp8g0BOfwPurza77OSIRAguPzaNbMi9fPO01B5nnRW1ib-O86C3GcFsEBR3m-P8F6BeYBq7F-nxvtOFj_flMmndLHR35..'},
        {'domain': '.taobao.com', 'expiry': 1711473174, 'httpOnly': False, 'name': 'tracknick', 'path': '/',
         'sameSite': 'None', 'secure': True, 'value': 'tb919827938'},
        {'domain': '.taobao.com', 'httpOnly': False, 'name': '_tb_token_', 'path': '/', 'sameSite': 'None',
         'secure': True, 'value': '7eb663b8efb38'},
        {'domain': '.taobao.com', 'httpOnly': True, 'name': '_samesite_flag_', 'path': '/', 'sameSite': 'None',
         'secure': True, 'value': 'true'}]
    bro = avoid_check()
    # 清除浏览器缓存和Cookie
    bro.delete_all_cookies()
    bro.get('https://login.taobao.com/member/login.jhtml')
    # 添加cookies
    for cookie in cookies:
        bro.add_cookie(cookie)
    # 搜索淘宝商品
    bro.get('https://www.taobao.com/')
    # 标签定位
    search_input = bro.find_element('id', value='q')
    # 搜索关键词
    search_input.send_keys(goods_word)
    # 点击搜索按钮
    btn = bro.find_element('class name', value='btn-search')
    btn.submit()
    sleep(3)
    # 执行一组js程序滚动页面置底
    for i in range(1, 3):
        bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        sleep(3)
    # 数据解析
    tree = etree.HTML(bro.page_source)
    goods_li_list = (tree.xpath('//div[@id="mainsrp-itemlist"]//div[@class="grid g-clearfix"]/div[1]/div'))
    # 最大页数
    max_page = ''.join(tree.xpath('//div[@class="total"]/text()'))

    for page in range(1, 3):
        # 点击下一页
        #page_input = bro.find_element(By.XPATH, '//div[@class="form"]/input')
        page_input = bro.find_element(By.XPATH, '//div[@class="next-pagination-pages"]/span[3]/input')
        page_input.clear()
        page_input.send_keys(page + 1)
        # 找到翻页按钮并点击
        page_button = bro.find_element(By.XPATH, '//div[@class="next-pagination-pages"]/button[3]/span')
        #print("爬取第", page, "页")
        page_button.click()
        # 等待页面加载完成
        sleep(2)
        # 执行一组js程序滚动页面置底
        for j in range(1, 3):
            bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(3)
        # 数据解析
        tree = etree.HTML(bro.page_source)
        goods_li_list = goods_li_list + \
                        (tree.xpath('//div[@id="mainsrp-itemlist"]//div[@class="grid g-clearfix"]/div[1]/div'))
    i = 0
    for li in goods_li_list:
        # 图片
        goods_img = 'https:' + ''.join(li.xpath('.//div[@class="pic"]/a/img/@data-src')).replace('\n', '')
        # 商品标题
        goods_title = ''.join(li.xpath('.//div[@class="row row-2 title"]/a//text()')).split('\n')
        goods_title = ''.join(goods_title).strip(' ')[0: 127]
        # 商品价格
        goods_price = li.xpath('.//div[@class="price g_price g_price-highlight"]/strong/text()')[0]
        if draw_num(goods_price) == '':
            goods_price = 0
        # 销量
        goods_sales = ''.join(li.xpath('.//div[@class="deal-cnt"]/text()')).replace('人付款', '')
        if not goods_sales:
            goods_sales = '未知'
        # 店铺名
        goods_shop = ''.join(li.xpath('.//div[@class="shop"]/a/span[2]/text()')).replace('\n', '')
        if not goods_shop:
            goods_shop = '未知'
        # 商品链接
        goods_link_nid = ''.join(li.xpath('.//div[@class="pic"]/a/@data-nid'))
        goods_link = 'https://item.taobao.com/item.htm?id=' + goods_link_nid
        # 平台
        goods_platform = '淘宝'
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
    tb_goods_info = crawler(goods_word=word)
    print(len(tb_goods_info), tb_goods_info)
