#!/usr/bin/env python3
""" lifo cache task file.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    FIFOCache class define fifo based cache methods
    """

    def __init__(self):
        """
        Init the class with parent class init method
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Method to cache a key-value pair.
        """
        if key is None or item is None:
            pass
        else:
            len = len(self.cache_data)
            if len >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[-1]))
                del self.cache_data[self.order[-1]]
                del self.order[-1]
            if key in self.order:
                del self.order[self.order.index(key)]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to a given key, or None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None

