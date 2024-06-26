#!/usr/bin/env python3
""" 2. LIFO Caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    uses LIFO algorithm in caching
    """
    def __init__(self):
        """
        Initiate new instance from LIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """
        set item within the key inside the cache
        """
        cache = self.cache_data
        last_key = list(cache.keys())[-1] if len(cache) > 0 else None
        if key is not None and item is not None:
            self.cache_data.update({
                key: item
            })
        if len(self.cache_data) > self.MAX_ITEMS:
            self.cache_data.pop(last_key)
            print('DISCARD: {}'.format(last_key))

    def get(self, key):
        """
        get value of the key from the cache
        """
        return self.cache_data.get(key, None) if key is not None else None
