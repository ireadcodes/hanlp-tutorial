import re
import heapq

from .word_info import WordInfo


class NewWordDiscover:
    def __init__(self, max_word_len, min_freq, min_entropy, min_aggregation):
        """
        :param max_word_len: 词语最长长度
        :param min_freq: 词语最低频率
        :param min_entropy: 词语最低信息熵
        :param min_aggregation: 词语最低互信息
        """
        self.max_word_len = max_word_len
        self.min_freq = min_freq
        self.min_entropy = min_entropy
        self.min_aggregation = min_aggregation

    def discover(self, docs, size):
        word_candidates = dict()
        total_length = 0
        delimiter = re.compile(r"[\s\d,.<>/?:;'\"\[\]{}()\|~!@#$%^&*\-_=+，。《》、？：；“”‘’｛｝【】（）…￥！—┄－]+")
        for doc in docs:
            doc = delimiter.sub('\0', doc)
            doc_length = len(doc)
            for i in range(doc_length):
                end = min(i + 1 + self.max_word_len, doc_length + 1)
                for j in range(i + 1, end):
                    word = doc[i: j]
                    if '\0' in word:
                        continue
                    if word not in word_candidates:
                        info = WordInfo(word)
                        word_candidates[word] = info
                    else:
                        info = word_candidates[word]
                    info.update(doc[i - 1] if i != 0 else '\0', doc[j] if j < doc_length else '\0')
            total_length += doc_length
        # 计算信息熵
        for info in word_candidates.values():
            info.compute_probability_entropy(total_length)
        # 计算互信息
        for info in word_candidates.values():
            info.compute_aggregation(word_candidates)
        # 过滤
        condition = lambda item: len(item.text.strip()) >= 2 and item.p >= self.min_freq and item.entropy >= self.min_entropy and item.aggregation >= self.min_aggregation
        word_info_list = filter(condition, word_candidates.values())
        # 排序
        return heapq.nlargest(size, word_info_list, key=lambda item: item.p)
