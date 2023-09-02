from django_redis import get_redis_connection


class RedisCacheTool:
    cache_con = get_redis_connection("default")

    def set_cache(self, key: str, value: str):
        self.cache_con.set(key, value)

    def get_cache(self, key: str) -> str:
        value = self.cache_con.get(key)
        return value

    def flush(self):
        self.cache_con.flushall()
