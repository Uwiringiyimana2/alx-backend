#!/usr/bin/python3
"""FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class"""
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_item = self.order.pop(0)
                del self.cache_data[oldest_item]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
