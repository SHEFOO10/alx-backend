#!/usr/bin/env python3
""" 4. MRU Caching """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    uses MRU algorithm
    """
    def __init__(self):
        """ Initiate a MRUCache Instance """
        super().__init__()
        self.key_access_order = []

    def put(self, key, item):
        """
        put item within the cache by the key
        """
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.key_access_order.remove(key)
                self.key_access_order.append(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    removed = self.key_access_order.pop()
                    del self.cache_data[removed]
                    print('DISCARD: {}'.format(removed))
                self.cache_data[key] = item
                self.key_access_order.append(key)

    def get(self, key):
        """
        get item with the given key
        """
        value = None
        if key is not None:
            value = self.cache_data.get(key, None)
            if value is not None:
                self.key_access_order.remove(key)
                self.key_access_order.append(key)
        return value
