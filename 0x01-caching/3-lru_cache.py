#!/usr/bin/env python3
""" 3. LRU Caching """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    uses LRU algoritm in cache
    """
    def __init__(self):
        """ Initiate LRUCache instance """
        super().__init__()
        self.key_access_order = []

    def put(self, key, item):
        """
        insert item within the key inside the cache
        """
        if key is not None and item is not None:
            # Check if key already exists
            if key in self.cache_data:
                # Update item and move key to end of access order
                self.cache_data[key] = item
                self.key_access_order.remove(key)
                self.key_access_order.append(key)
            else:
                # Add new item and key to cache
                if len(self.cache_data) >= self.MAX_ITEMS:
                    # Remove least recently used item
                    lru_key = self.key_access_order.pop(0)
                    del self.cache_data[lru_key]
                    print('DISCARD: {}'.format(lru_key))
                self.cache_data[key] = item
                self.key_access_order.append(key)

    def get(self, key):
        """
        get item from the cache with the key
        """
        value = None
        if key is not None:
            value = self.cache_data.get(key, None)
            if value is not None:
                self.key_access_order.remove(key)
                self.key_access_order.append(key)
        return value
