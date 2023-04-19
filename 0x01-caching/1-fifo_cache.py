#!/usr/bin/env python3
""" Fifo cache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    This class define a fifo based caching methods
    """

    def __init__(self):
        """
        Init the class with parent class init method
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Method to cache a key-value pair
        """
        if key is None or item is None:
            pass
        else:
            len = len(self.cache_data)
            if len >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            self.order.append(key)
            self.cache_data[key] = item


    def get(self, key):
        """
        Fetches value linked to a key.
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
