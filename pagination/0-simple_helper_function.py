#!/usr/bin/env python3
"""
simple helper fucntion
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index range fucntion
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
