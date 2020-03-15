import redis
conn = redis.StrictRedis(host="localhost", port=6379, charset="utf-8", decode_responses=True)

conn.hset('prediction','GuanYin',25.83)
conn.hset('prediction','PingZhen',19.02)
conn.hset('prediction','LongTan',17.83)
conn.hset('prediction','JhongLi',27.77)
conn.hset('prediction','TaoYuan',21.09)

print(conn.hgetall('air_quality'))

print(conn.hvals('air_quality'))



