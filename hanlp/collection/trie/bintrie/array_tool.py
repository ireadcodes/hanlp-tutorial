from typing import List

from .base_node import BaseNode


class ArrayTool:
    @staticmethod
    def binary_search_node(branches: List[BaseNode], node: BaseNode) -> int:
        high = len(branches) - 1
        if len(branches) < 1:
            return high
        low = 0
        while low <= high:
            mid = (low + high) >> 1
            mid_node = branches[mid]
            if mid_node.c < node.c:
                low = mid + 1
            elif mid_node.c > node.c:
                high = mid - 1
            else:
                return mid
        return -(low + 1)

    @staticmethod
    def binary_search_char(branches: List[BaseNode], c: str) -> int:
        high = len(branches) - 1
        if len(branches) < 1:
            return high
        low = 0
        while low <= high:
            mid = (low + high) >> 1
            mid_node = branches[mid]
            if mid_node.c < c:
                low = mid + 1
            elif mid_node.c > c:
                high = mid - 1
            else:
                return mid
        return -(low + 1)
