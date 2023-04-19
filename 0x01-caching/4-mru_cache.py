#!/usr/bin/env python3
""" MRU based caching module.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUcache class defines mru based methods.
    """

    def __init__(self):
        """
        Init the class. Along with super class init method
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Cache method for a key-value pair
        """
        if key is None or item is None:
            pass
        else:
            len = len(self.cache_data)
            if len >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usage[-1]))
                del self.cache_data[self.usage[-1]]
                del self.usage[-1]
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get key val or none
        """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            return self.cache_data[key]
        return None
