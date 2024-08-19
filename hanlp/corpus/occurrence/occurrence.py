# 词共现统计，最多统计到三阶共现
from typing import List

from hanlp.collection.trie.bintrie.bin_trie import BinTrie
from hanlp.corpus.occurrence.term_frequency import TermFrequency


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

    def add_all(self, term_list: List[str]):
        for term in term_list:
            self.add_term(term)

    def add_term(self, key: str):
        value = self.trie_single.get(key)
        if value is None:
            value = TermFrequency(key)
            self.trie_single.put(key, value)
        else:
            value.increase_one()
        self.total_term += 1

    def compute(self):
        pass

