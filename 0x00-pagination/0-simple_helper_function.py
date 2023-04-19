#!/usr/bin/env python3
"""
Task zero file for index_range function definition
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes in two integer variables
    Return:
        tuple(start_index, end_index)
    """
    starting, ending = 0, 0
    for i in range(page):
        starting = ending
        ending += page_size

    return (starting, ending)
