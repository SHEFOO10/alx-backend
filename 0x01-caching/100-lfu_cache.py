#!/usr/bin/env python3
""" 5. LFU Caching """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    uses LFU algorithm
    """
    def __init__(self):
        """ Initiate an Instance of LFUCache """
        super().__init__()
        self.freq_dict = {}
        self.key_access_order = []

    def put(self, key, item):
        """
        put the data inside the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.freq_dict[key] = 1
                self.key_access_order.remove(key)
                self.key_access_order.append(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    # Remove least frequently used item(s)
                    min_freq = min(self.freq_dict.values())
                    lfu_keys = [k for k, v in self.freq_dict.items()
                                if v == min_freq
                                ]
                    lfu = min(lfu_keys,
                              key=lambda k: self.key_access_order.index(k)
                              )
                    del self.cache_data[lfu]
                    del self.freq_dict[lfu]
                    self.key_access_order.remove(lfu)
                    print('DISCARD: {}'.format(lfu))
                self.cache_data[key] = item
                self.freq_dict[key] = 1
                self.key_access_order.append(key)

    def get(self, key):
        """
        get item with the passed key
        from cache
        """
        value = None
        if key is not None:
            value = self.cache_data.get(key, None)
            if value is not None:
                self.freq_dict[key] += 1
                self.key_access_order.remove(key)
                self.key_access_order.append(key)
        return value
