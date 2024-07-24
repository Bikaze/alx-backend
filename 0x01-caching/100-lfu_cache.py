#!/usr/bin/python3
"""
This module defines a LFUCache class which inherits from BaseCaching.
It represents a caching system that discards the least frequently used
item when it exceeds its limit. If multiple items are least frequently used,
the least recently used among them is discarded.
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching and is a caching system.
    It discards the least frequently used item (LFU) when the cache exceeds
    its limit.

    If there is more than one least frequently used item, the least recently
    used (LRU) among them is discarded.
    """

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.key_usage_count = {}
        self.key_order = []

    def put(self, key, item):
        """
        Add an item in the cache.
        If the cache exceeds the max limit, remove the least frequently
        used item.

        If there is more than one, remove the least recently used among them.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.key_usage_count[key] += 1
                self.key_order.remove(key)
            else:
                self.key_usage_count[key] = 0
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                """Sort keys by usage count, then by their order to find
                the LFU/LRU"""
                lfu_keys = sorted(self.key_order,
                                  key=lambda x: (self.key_usage_count[x],
                                                 self.key_order.index(x)))
                lfu_key = lfu_keys[0]
                self.cache_data.pop(lfu_key)
                self.key_order.remove(lfu_key)
                self.key_usage_count.pop(lfu_key)
                print(f"DISCARD: {lfu_key}")
            self.key_order.append(key)

    def get(self, key):
        """
        Get an item by key.
        Return None if key is None or key doesn't exist in cache_data.
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            self.key_usage_count[key] += 1
            if key in self.key_order:
                self.key_order.remove(key)
                self.key_order.append(key)
            return self.cache_data[key]
