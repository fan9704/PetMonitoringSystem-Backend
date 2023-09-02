from django.test import TestCase
from api.utils.cacheTool import RedisCacheTool


class TestCacheOperations(TestCase):
    def setUp(self):
        self.cache = RedisCacheTool()

    def tearDown(self):
        self.cache.flush()

    def test_cache_set_and_get(self):
        self.cache.set_cache('keyName', 'value')
        cached_value = self.cache.get_cache('keyName')
        self.assertEqual(cached_value, b'value')

    def test_cache_nonexistent_key(self):
        cached_value = self.cache.getCache('nonExistentKey')
        self.assertIsNone(cached_value)
