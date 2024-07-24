#!/usr/bin/env python3
"""Least frequently used (LFU) caching module."""
from collections import OrderedDict, defaultdict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class"""
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.freq = defaultdict(int)
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.usage_order.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.freq.values())
                lfu_keys = [k for k, f in self.freq.items() if f == min_freq]

                if len(lfu_keys) > 1:
                    lru = next(k for k in self.usage_order if k in lfu_keys)
                else:
                    lru = lfu_keys[0]

                del self.cache_data[lru]
                del self.freq[lru]
                self.usage_order.pop(lru)
                print(f"DISCARD: {lru}")

            self.cache_data[key] = item
            self.freq[key] = 1
            self.usage_order[key] = None

    def get(self, key):
        """Retrieves an item by key."""
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        self.usage_order.move_to_end(key)
        return self.cache_data[key]
