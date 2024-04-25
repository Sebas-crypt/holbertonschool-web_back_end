#!/usr/bin/env python3
"""
complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List [Union[int, float]]) -> float:
    """
    return a sum od all nums inside a list
    """
    return sum(mxd_lst)
