"""
自定义数据（[{},{}]）存储到数据库组件,如果想用这个组件，你需要做如下几件事：

    # 定义连接列表包含（[host, user, password, database]）
    conn = ['127.0.0.1', 'root', '111111', 'grab_goods']
    # 书写sql语句（insert into 表名(field1,field2...) values(%s..)）
    sql = 'insert into app01_goods(goods_img,goods_title,goods_price,goods_sales,shop_title,shop_platform,goods_link,grab_time) ' \
          'values(%s,%s,%s,%s,%s,%s,%s,%s)'
    # 实例化组件对象
    to_sql = ToSql(jd_goods_info, conn=conn)
    # 调用对象中dump()函数插入数据
    to_sql.dump(sql=sql)
"""
import pymysql


class ToSql(object):
    def __init__(self, info, conn):
        """
        :param info: 需转存数据，数据格式[{},{},{}]
        :param conn: 连接数据库的配置数据包含[host, user, password, database]，数据格式[]
        """
        self.info = info
        self.conn = conn

    def dump(self, sql):
        """
        :param sql: 执行的sql语句，格式字符串
        :return: None
        """
        list_data = []
        conn = pymysql.connect(host=self.conn[0], user=self.conn[1], password=self.conn[2], database=self.conn[3])
        cur = conn.cursor()
        for dic_data in self.info:
            for i, j in dic_data.items():
                list_data.append(j)
            cur.execute(sql, list_data)
            conn.commit()
            list_data.clear()
        cur.close()
        conn.close()
