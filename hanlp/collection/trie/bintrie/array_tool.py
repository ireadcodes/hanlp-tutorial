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
            if ord(mid_node.c) < ord(node.c):
                low = mid + 1
            elif ord(mid_node.c) > ord(node.c):
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
            if ord(mid_node.c) < ord(c):
                low = mid + 1
            elif ord(mid_node.c) > ord(c):
                high = mid - 1
            else:
                return mid
        return -(low + 1)
