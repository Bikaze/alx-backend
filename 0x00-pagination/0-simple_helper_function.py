#!/usr/bin/env python3
"""
This module defines a simple helper function for calculating the
and end index for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for a page of items.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and the end index
        of the items for the current page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
