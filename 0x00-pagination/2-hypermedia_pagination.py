#!/usr/bin/env python3
"""
This module provides a Server class to paginate a database of popular
baby names stored in a CSV file.
"""

import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Fetch a page of the dataset with specified size.

        Args:
            page (int): The page number.
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows from the dataset for the specified page.
        """
        assert isinstance(page, int) and page > 0, "Page must \
            be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size \
            must be a positive integer"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]\
            if start_index < len(dataset) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Fetch a page of the dataset and provide additional pagination details.

        Args:
            page (int): The page number.
            page_size (int): The number of items per page.

        Returns:
            dict: A dictionary with pagination details and the page's data.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
