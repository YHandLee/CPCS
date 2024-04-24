from app01.grab_goods.jd_goods import crawler as jd_craw
from app01.grab_goods.sn_goods import crawler as sn_craw
from app01.grab_goods.tb_goods import crawler as tb_craw
from app01.utils.goods_to_sql import ToSql

if __name__ == "__main__":
    word = input('请输入需要查询的商品：')
    print("--------正在爬取京东数据...--------")
    jd_goods_info = jd_craw(goods_word=word)
    print("--------爬取京东数据完成！！！--------")
    print("--------正在爬取苏宁易购数据...--------")
    sn_goods_info = sn_craw(goods_word=word)
    print("--------爬取苏宁易购数据完成！！！--------")
    print("--------正在爬取淘宝数据...--------")
    tb_goods_info = tb_craw(goods_word=word)
    print("--------爬取淘宝数据完成！！！--------")
    goods_info = jd_goods_info + sn_goods_info + tb_goods_info
    print("本次总共爬取", len(goods_info), "条数据。")
    print("正在将数据保存到数据库...")
    # 转存到数据库
    conn = ['127.0.0.1', 'root', '111111', 'grab_goods']
    sql = 'insert into app01_goods(goods_img,goods_title,goods_price,goods_sales,shop_title,' \
          'shop_platform,goods_link,grab_time) ' \
          'values(%s,%s,%s,%s,%s,%s,%s,%s)'
    to_sql = ToSql(goods_info, conn=conn)
    to_sql.dump(sql=sql)
    print("已全部保存到数据库")
