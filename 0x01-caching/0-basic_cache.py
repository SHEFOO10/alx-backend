#!/usr/bin/env python3
""" 0. Basic dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Dictionary Cache
    """
    def put(self, key, item):
        """
        put item with the key in the cache
        """
        if key is not None and item is not None:
            self.cache_data.update({
                key: item
            })

    def get(self, key):
        """ get value of the passed key """
        return self.cache_data.get(key, None) if key is not None else None
