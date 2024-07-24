#!/usr/bin/env python3
"""
This module defines a BasicCache class which inherits from BaseCaching.
It represents a basic caching system without a limit on the number of
items it can store.
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A basic cache system that stores key-value pairs without any limit.
    Inherits from BaseCaching class.
    """

    def put(self, key, item):
        """
        Add an item to the cache.
        Args:
            key: Key under which the item is stored. If key or item is None,
            does nothing.
            item: Item to store in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

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
