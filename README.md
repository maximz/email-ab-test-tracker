?∞ docker run -it --link maximz-redis:redis --rm redis bash
root@a8183d604a62:/data# redis-cli -h redis
redis:6379> ping
PONG