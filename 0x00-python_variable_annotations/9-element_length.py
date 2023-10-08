#!/usr/bin/env python3
"""annotation module"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """annotation function"""
    return [(i, len(i)) for i in lst]
