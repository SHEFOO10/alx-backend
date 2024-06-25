""" 2. Hypermedia pagination """
import csv
import math
from typing import List, Tuple, Dict, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return index range based on page and page_size """
    return (
            (page - 1) * page_size,
            page * page_size
            )


class Server:
    """
    Server class to paginate a database of popular baby names.
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
        """ get the page """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(
        self,
        page: int = 1,
        page_size: int = 10,
    ) -> Dict[str, Union[int, List[List], None]]:
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = None if (page + 1) > total_pages else page + 1
        prev_page = page - 1 if (page - 1) > 0 else None
        return {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': math.ceil(len(self.dataset()) / page_size)
        }
