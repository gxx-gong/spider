import pymysql

def conn_mysql():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='mytest', charset='utf8')
    cur = conn.cursor()
    sql = 'insert into doubantop_week values(4,"你好")'
    cur.execute(sql)
    conn.commit()
    result = cur.fetchall()
    cur.close()
    conn.close()
    print(result)

if __name__ == '__main__':
    conn_mysql()
