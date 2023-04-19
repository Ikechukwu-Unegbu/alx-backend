#!/usr/bin/env python3
"""BaseCaching task file
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This class defines methods for caching information in key-value
    Methods:
        put(key, item) - method to cache key value pair
        get(key) - method to retriev value of given key
    """

    def __init__(self):
        """
        Init the class with parent class init method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        This method stores a key value-pair
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns value linked to a key if the key exists.
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None

