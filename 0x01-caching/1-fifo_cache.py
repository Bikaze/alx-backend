#!/usr/bin/env python3
"""
This module defines a FIFOCache class which inherits from BaseCaching.
It represents a caching system that discards the least recently added
item when it exceeds its limit.
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    A FIFO cache system that stores key-value pairs up to a maximum number
    defined in BaseCaching.MAX_ITEMS.
    Inherits from BaseCaching class.
    """

    def __init__(self):
        """
        Initialize the class instance, calling the parent class init to
        set up the cache_data dictionary.
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item to the cache using FIFO strategy.
        Args:
            key: Key under which the item is stored. If key or item is None,
            does nothing.
            item: Item to store in the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = self.queue.pop(0)
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.
        Args:
            key: Key for which the item should be returned. If key is None
            or does not exist, returns None.
        Returns:
            The value stored in cache_data linked to key, or None if key is
            None or key does not exist.
        """
        return self.cache_data.get(key)
