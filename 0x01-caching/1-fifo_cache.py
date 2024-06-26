#!/usr/bin/env python3
""" 1. FIFO caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Uses FIFO algorithm in Caching
    """
    def __init__(self):
        """ Initialize new FIFOCache Instance """
        super().__init__()

    def put(self, key, item):
        """
        insert data into the cache
        """
        if key is not None and item is not None:
            self.cache_data.update({
                key: item
            })
        if len(self.cache_data.keys()) > self.MAX_ITEMS:
            key = next(iter(self.cache_data))
            self.cache_data.pop(key)
            print('DISCARD: {}'.format(key))

    def get(self, key):
        """
        get value if the passed key from cache
        """
        return self.cache_data.get(key, None) if key is not None else None
