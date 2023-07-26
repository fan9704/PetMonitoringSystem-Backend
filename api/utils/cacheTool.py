from django_redis import get_redis_connection

cacheCon = get_redis_connection("default")
cacheCon.set('keyName', 'value')
value = cacheCon.get('keyName')
