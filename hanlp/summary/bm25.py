import math
from typing import List, Dict


class BM25:
    def __init__(self, docs: List[List[str]]):
        self.k1 = 1.5
        self.b = 0.75
        # 拆分为[句子[单词]]形式的文档
        self.docs = docs
        # 文档句子的个数
        self.D = len(docs)
        # 文档句子的平均长度
        self.avgdl = 0
        for sentence in self.docs:
            self.avgdl += len(sentence)
        self.avgdl /= self.D
        # 文档中每个句子中的每个词与词频
        self.f: List[Dict[str, int]] = [{} for _ in range(self.D)]
        # 文档中全部词语与出现在几个句子中
        self.df: Dict[str, int] = dict()
        # IDF
        self.idf: Dict[str, float] = dict()
        self.init()

    def init(self):
        index = 0
        for sentence in self.docs:
            tf = dict()
            for word in sentence:
                freq = tf.get(word, 0)
                freq += 1
                tf[word] = freq
            # 记录每个句子中每个词汇的频数
            self.f[index] = tf
            for word in tf.keys():
                freq = self.df.get(word, 0)
                freq += 1
                # 计算每个词的词频，用于后面计算IDF
                self.df[word] = freq
            index += 1
        for word, freq in self.df.items():
            # 计算IDF
            self.idf[word] = math.log(self.D - freq + 0.5) - math.log(freq + 0.5)

    def sim(self, sentence: List[str], index: int) -> float:
        score = 0
        for word in sentence:
            if word not in self.f[index]:
                continue
            # 被检索文档包含词汇的长度
            d = len(self.docs[index])
            tf = self.f[index][word]
            # BM25核心公式
            score += (self.idf[word] * tf * (self.k1 + 1) / (tf + self.k1 * (1 - self.b + self.b * d / self.avgdl)))
        return score

    def sim_all(self, sentence: List[str]) -> List[float]:
        scores = [0.0] * self.D
        # 计算sentence与docs中每个文档的相似度
        for i in range(self.D):
            scores[i] = self.sim(sentence, i)
        return scores

