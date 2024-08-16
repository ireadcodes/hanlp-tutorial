# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-05-25 17:25
# 《自然语言处理入门》2.4 字典树
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from typing import Dict


# 字典树的节点实现
class Node(object):
    def __init__(self, value: str):
        # 保存"自然"时，_children的键是"自"，值是"然"的Node对象
        self._children: Dict[str, Node] = {}
        self._value: str = value

    # 把子节点连接到父节点上
    def _add_child(self, char: str, value: str, overwrite: bool = False):
        child = self._children.get(char)
        if child is None:
            child = Node(value)
            self._children[char] = child
        # 根据overwrite来决定是否覆盖child的值
        elif overwrite:
            child._value = value
        return child


# 字典树的增删改查实现
class Trie(Node):
    def __init__(self) -> None:
        super().__init__(None)

    def __contains__(self, key):
        return self[key] is not None  # __getitem__

    def __getitem__(self, key):
        state = self
        for char in key:
            state = state._children.get(char)
            if state is None:
                return None
        return state._value

    def __setitem__(self, key, value):
        state = self
        for i, char in enumerate(key):
            # 判断是否是key的最后一个字
            if i < len(key) - 1:
                state = state._add_child(char, None, False)
            else:
                state = state._add_child(char, value, True)


if __name__ == '__main__':
    trie = Trie()
    # 增
    trie['自然'] = 'nature'  # __setitem__
    trie['自然人'] = 'human'
    trie['自然语言'] = 'language'
    trie['自语'] = 'talk	to oneself'
    trie['入门'] = 'introduction'
    assert '自然' in trie  # __contains__
    # 删
    trie['自然'] = None
    assert '自然' not in trie
    # 改
    trie['自然语言'] = 'human language'
    assert trie['自然语言'] == 'human language'
    # 查
    assert trie['入门'] == 'introduction'
