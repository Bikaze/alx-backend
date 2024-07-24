#!/usr/bin/python3
"""
This module defines a MRUCache class which inherits from BaseCaching.
It represents a caching system that discards the most recently used
item when it exceeds its limit.
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and is a caching system.
    It discards the most recently used item (MRU) when the cache exceeds its
    limit.
    """

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        Add an item in the cache.
        If the cache exceeds the max limit, remove the most recently used item.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.key_order.remove(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                mru_key = self.key_order.pop()  # The last item is the MRU
                self.cache_data.pop(mru_key)
                print(f"DISCARD: {mru_key}")
            self.key_order.append(key)

    def get(self, key):
        """
        Get an item by key.
        Return None if key is None or key doesn't exist in cache_data.
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            # Move the accessed key to the end to maintain MRU order
            if key in self.key_order:
                self.key_order.remove(key)
                self.key_order.append(key)
            return self.cache_data[key]
