from hanlp.collection.trie.bintrie.base_node import BaseNode, Status


# 首字散列其余二分的前缀树
class BinTrie(BaseNode):

    def __init__(self):
        super().__init__()
        self.child = [None] * (65535 + 1)
        self.status = Status.NOT_WORD_1
        self.size = 0

    def put(self, key: str, value):
        if len(key) == 0:
            return
        branch = self
        # 除了最后一个字外，都是继续
        for i in range(len(key) - 1):
            branch.add_child(BaseNode(key[i], Status.NOT_WORD_1, None))
            branch = branch.get_child(key[i])
        # 最后一个字加入时属性为end
        if branch.add_child(BaseNode(key[-1], Status.WORD_END_3, value)):
            self.size += 1

    def get(self, key: str):
        branch = self
        for c in key:
            if branch is None:
                return None
            branch = branch.get_child(c)
        if branch is None:
            return None
        if not (branch.status == Status.WORD_END_3 or branch.status == Status.WORD_MIDDLE_2):
            return None
        return branch.value

    def add_child(self, node: 'BaseNode') -> bool:
        add = False
        c = node.c
        target = self.get_child(c)
        if target is None:
            self.child[ord(c)] = node
            add = True
        else:
            if node.status == Status.UNDEFINED_0:
                if target.status != Status.NOT_WORD_1:
                    target.status = Status.NOT_WORD_1
                    add = True
            elif node.status == Status.NOT_WORD_1:
                if target.status == Status.WORD_END_3:
                    target.status = Status.WORD_MIDDLE_2
            elif node.status == Status.WORD_END_3:
                if target.status != Status.NOT_WORD_1:
                    target.status = Status.WORD_MIDDLE_2
                if target.value is None:
                    add = True
                target.value = node.value
        return add

    def get_child(self, c: str):
        return self.child[ord(c)]
