#!/usr/bin/python3
""" Basic Caching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """a caching system
      must use self.cache_data
    """
    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """the dictionary self.cache_data the item value for the key key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
