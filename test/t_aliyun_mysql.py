import pymysql

conn = pymysql.Connect(
    host='121.199.63.71',
    user='ygadmin',
    password='yg1176',
    port=3306,
    db='yg_api_db',
    charset='utf8'
)

print('ok')