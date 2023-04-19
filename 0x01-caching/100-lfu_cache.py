#!/usr/bin/env python3
""" LFU Module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache defines a LFU caching system
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.usage = []
        self.frequency = {}

    def put(self, key, item):
        """
        Method to cache a key-value pair using the LFU algorithm
        """
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            lfu_keys = [k for k, v in self.frequency.items() if v == min(self.frequency.values())]
            discard = lfu_keys[0]
            del self.cache_data[discard]
            self.usage.remove(discard)
            del self.frequency[discard]

        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

        self.usage.append(key)
        self.cache_data[key] = item


    def get(self, key):
        """
        Get the value of a key or NONE.
        """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
