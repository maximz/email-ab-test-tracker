
See testing.md for how to run

Usage:

* `/pixel/[site name]/[user name]/pixel.png` is tracking pixel
* `/mark/[mark id]` is to mark a boolean value
* `/admin` is admin panel

To upgrade database when deploying to prod, run: `python manage.py db upgrade` to apply the migration.


# old
?∞ docker run -it --link maximz-redis:redis --rm redis bash
root@a8183d604a62:/data# redis-cli -h redis
redis:6379> ping
PONG