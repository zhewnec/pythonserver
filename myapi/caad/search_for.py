import pymssql
import json

def sqlserver( sql):
    conn = pymssql.connect(host='115.231.160.234', port=1433, user='netteam', password='2n4SGVQcmqeY',
                           database='Caad.Viss.New', charset='utf8')
    cur = conn.cursor(as_dict=True)
    cur.execute(sql)
    data = cur.fetchone()
    cur.close()
    conn.close()
    return json.dumps(data, ensure_ascii=False, encoding='UTF-8')


def test_sqlserver(sql):
    conn = pymssql.connect(host='172.16.2.116', port=1433, user='SysCaad', password='P@ssw0rd',
                           database='Caad.Viss.New', charset='utf8')
    cur = conn.cursor(as_dict=True)
    cur.execute(sql)
    data = cur.fetchone()
    cur.close()
    conn.close()

    return json.dumps(data, ensure_ascii=False, encoding='UTF-8')