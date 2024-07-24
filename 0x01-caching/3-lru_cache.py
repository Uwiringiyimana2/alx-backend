#!/usr/bin/python3
"""LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """cache data"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru = self.order.pop(0)
                print(f"DISCARD: {lru}")
                del self.cache_data[lru]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key)
