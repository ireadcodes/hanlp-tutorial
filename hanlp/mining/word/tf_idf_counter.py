import heapq
from typing import List, Dict, Set, Tuple

from hanlp.mining.word.tf_idf import TfIdf


class TfIdfCounter:
    def __init__(self):
        self.tf_map: Dict[str, Dict[str, float]] = dict()
        self.tfidf_map: Dict[str, Dict[str, float]] = dict()
        self.idf: Dict[str, float] = dict()

    def add(self, uuid: str, words: List[str]):
        # 这里是计算每篇文章的中的词频
        tf = TfIdf.tf_natural(words)
        # 这里使用tf_map的键存储词条相当于对同一篇文章中的相同词汇去重了
        self.tf_map[uuid] = tf
        self.idf = None

    def compute(self):
        self.idf = TfIdf.idf_from_tfs(self.tf_map.values())
        for k, v in self.tf_map.items():
            tfidf = TfIdf.tfidf(v, self.idf)
            self.tfidf_map[k] = tfidf
        return self.tfidf_map

    def documents(self) -> Set[str]:
        return set(self.tf_map.keys())

    def get_keywords_of(self, uuid: str, size: int) -> List[Tuple[str, float]]:
        tfidfs = self.tfidf_map[uuid]
        return heapq.nlargest(size, tfidfs.items(), key=lambda item: item[1])

    def get_keywords_with_tfidf(self, document: List[str], size: int) -> List[Tuple[str, float]]:
        if len(self.idf) == 0:
            self.compute()
        tfidfs = TfIdf.tfidf(TfIdf.tf_natural(document), self.idf)
        return heapq.nlargest(size, tfidfs.items(), key=lambda item: item[1])
