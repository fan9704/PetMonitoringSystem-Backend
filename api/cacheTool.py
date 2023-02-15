# from django.core.cache import cache # django built-in cache
# cache.set("keyName", "value", timeout=25)
# cache.get("keyName")

from django_redis import get_redis_connection

cacheCon = get_redis_connection("default")
cacheCon.set('keyName', 'value')
value = cacheCon.get('keyName')
