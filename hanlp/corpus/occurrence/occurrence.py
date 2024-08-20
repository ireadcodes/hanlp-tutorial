# 词共现统计，最多统计到三阶共现
from typing import List

from hanlp.collection.trie.bintrie.bin_trie import BinTrie
from hanlp.corpus.occurrence.pair_frequency import PairFrequency
from hanlp.corpus.occurrence.term_frequency import TermFrequency
from hanlp.corpus.occurrence.tria_frequency import TriaFrequency

# 两个词的正向连接符 中国 RIGHT 人民
RIGHT = '\u0000'
# 两个词的逆向连接符 人民 LEFT 中国
LEFT = '\u0001'


class Occurrence:
    def __init__(self):
        # 2 gram的pair
        self.trie_pair = BinTrie()
        # 词频统计用的储存结构
        self.trie_single = BinTrie()
        # 三阶储存结构
        self.trie_tria = BinTrie()
        # 全部单词数量
        self.total_term = 0
        # 全部接续数量，包含正向和逆向
        self.total_pair = 0
        # 软缓存一个pair的set
        self.entry_set_pair = set()

    def add_all(self, term_list: List[str]):
        for term in term_list:
            self.add_term(term)
        first = None
        for current in term_list:
            if first is not None:
                self.add_pair(first, RIGHT, current)
            first = current
        for i in range(2, len(term_list)):
            self.add_tria(term_list[i - 2], term_list[i - 1], term_list[i])

    def add_term(self, key: str):
        value = self.trie_single.get(key)
        if value is None:
            value = TermFrequency(key)
            self.trie_single.put(key, value)
        else:
            value.increase_one()
        self.total_term += 1

    def add_pair(self, first, delimiter, second):
        key = first + delimiter + second
        value = self.trie_pair.get(key)
        if value is None:
            value = PairFrequency.create_pair(first, delimiter, second)
            self.trie_pair.put(key, value)
        else:
            value.increase_one()
        self.total_pair += 1

    def add_tria(self, first, second, third):
        key = first + RIGHT + second + RIGHT + third
        value = self.trie_tria.get(key)
        if value is None:
            value = TriaFrequency.create_trie(first, RIGHT, second, third)
            self.trie_tria.put(key, value)
        else:
            value.increase_one()

    def compute(self):
        self.entry_set_pair = self.trie_pair.entry_set()
        total_mi = 0
        total_le = 0
        total_re = 0
        for entry in self.entry_set_pair:
            value = entry.value
