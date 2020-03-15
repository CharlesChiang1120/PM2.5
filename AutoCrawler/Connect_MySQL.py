import pymysql
import os
import ssl


# used to fix Python SSL CERTIFICATE_VERIFY_FAILED
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

db = pymysql.connect(host='localhost', port=3306, user='root', db='Air_pollution', charset='utf8')
cursor = db.cursor()


cursor.execute("SELECT * FROM LongTan_real_time_2019 ORDER BY ID DESC LIMIT 1")

# 獲取最新資料
PingZhen_real_time_2019 = cursor.fetchone()

# 關閉連線
db.close()

print(PingZhen_real_time_2019)
