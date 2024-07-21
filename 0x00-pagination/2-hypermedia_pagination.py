#!/usr/bin/env python3
"""index_range"""
import csv
import math
from typing import Tuple, List, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index_range that takes two integer arguments page and page_size
     return a tuple of size two containing a start index and an end index
    """
    return (page - 1) * page_size, page * page_size


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get pages"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        start_idx, end_idx = index_range(page, page_size)
        data = self.dataset()

        if start_idx >= len(data):
            return []

        return data[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[Any, Any]:
        """get_hyper"""
        data = self.get_page(page, page_size)
        prev_page = page - 1 if page > 1 else None
        start_idx, end_idx = index_range(page, page_size)

        next_page = page + 1 if end_idx < len(self.dataset()) else None
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
