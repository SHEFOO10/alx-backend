#!/usr/bin/env python3
""" 1. Simple pagination """
import csv
import math
from typing import List


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
        assert (page > 0 and isinstance(page, int))
        assert (page > 0 and isinstance(page_size, int))
        first_index, end = index_range(page, page_size)
        try:
            result = self.dataset()[first_index:end]
        except IndexError:
            return []


def index_range(page, page_size):
    """ return index range based on page and page_size """
    return (
            (page - 1) * page_size,
            page * page_size
            )
