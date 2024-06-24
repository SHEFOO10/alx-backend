#!/usr/bin/env python3
""" 1.Simple helper function """


def index_range(page, page_size):
    """ return index range based on page and page_size """
    return (
            (page - 1) * page_size,
            page * page_size
            )
