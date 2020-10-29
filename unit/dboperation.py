import pymysql


class MysqlConnection:

    def __init__(self, host='172.17.4.234', user='liran', password='123456', database='crm', port=3306, charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset
    def open(self):
        self.conn = pymysql.Connection(host=self.host, user=self.user, password=self.password,
                                       database=self.database, port=self.port,charset=self.charset)
        #创建游标
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def search_all(self,sql):
        self.open()
        try:
            self.cur.execute(sql)
            res = self.cur.fetchall()
            print(res)
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            self.close()


    def update_operation(self,sql):
        self.open()
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            print('operation success~')
        finally:
            self.close()
        return None

    def delete_operation(self,sql):
        self.open()
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            print('operation success~')
        finally:
            self.close()

    def add_operation(self):
        pass

    def close(self):
        self.cur.close()
        self.conn.close()


