from enum import Enum
from typing import List, Set


class Status(Enum):
    UNDEFINED_0 = 0
    NOT_WORD_1 = 1
    WORD_MIDDLE_2 = 2
    WORD_END_3 = 3


class BaseNode:
    def __init__(self, c='', status=None, value=None):
        # 节点代表的字符
        self.c = c
        # 节点状态
        self.status = status
        # 节点代表的值
        self.value = value
        # 子节点
        self.child: List[BaseNode] = list()

    def add_child(self, node: 'BaseNode') -> bool:
        add = False
        from hanlp.collection.trie.bintrie.array_tool import ArrayTool
        index = ArrayTool.binary_search_node(self.child, node)
        if index >= 0:
            target = self.child[index]
            if node.status == Status.UNDEFINED_0:
                if target.status != Status.NOT_WORD_1:
                    target.status = Status.NOT_WORD_1
                    target.value = None
                    add = True
            elif node.status == Status.NOT_WORD_1:
                if target.status == Status.WORD_END_3:
                    target.status = Status.WORD_MIDDLE_2
            elif node.status == Status.WORD_END_3:
                if target.status != Status.WORD_END_3:
                    target.status = Status.WORD_MIDDLE_2
                if target.value is None:
                    add = True
                target.value = node.value
        else:
            new_child = [BaseNode()] * (len(self.child) + 1)
            insert = -(index + 1)
            new_child[:insert] = self.child[:insert]
            new_child[insert + 1:] = self.child[insert:]
            new_child[insert] = node
            self.child = new_child
            add = True
        return add

    def get_child(self, c: str) -> 'BaseNode':
        if self.child is None:
            return None
        from hanlp.collection.trie.bintrie.array_tool import ArrayTool
        index = ArrayTool.binary_search_char(self.child, c)
        if index < 0:
            return None
        return self.child[index]

    def walk(self, s: str, entry_set: Set['TrieEntry']):
        s += self.c
        if self.status == Status.WORD_MIDDLE_2 or self.status == Status.WORD_END_3:
            entry_set.add(TrieEntry(s, self.value))
        if self.child is None:
            return
        for node in self.child:
            if node is None:
                continue
            node.walk(s, entry_set)


class TrieEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
