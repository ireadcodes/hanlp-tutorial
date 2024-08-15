import math
from typing import List, Dict, Iterable


class TfIdf:

    @staticmethod
    def tf_natural(document: List[str]) -> Dict[str, float]:
        tf_temp = dict()
        for term in document:
            f = tf_temp[term] if term in tf_temp else 0
            tf_temp[term] = f + 1
        return tf_temp

    @classmethod
    def idf_from_tfs(cls, tfs: Iterable[Dict[str, float]]) -> Dict[str, float]:
        key_set = [tf.keys() for tf in tfs]
        return cls.idf(key_set, True, True)

    @staticmethod
    def idf(document_vocabs: Iterable[Iterable[str]], smooth: bool, add_one: bool) -> Dict[str, float]:
        """
        :param document_vocabs: 词表
        :param smooth: 平滑参数，视作额外有一个文档，该文档含有smooth个每个词语
        :param add_one: tf-idf加一平滑
        :return:
        """
        # 这里的df计算词汇在整个语料库中的词频，因为前面对单篇文章的词汇去重了，所以就得到了包含该词条的文档数量
        df = dict()
        d = 1 if smooth else 0
        a = 1 if add_one else 0
        n = d
        for document_vocab in document_vocabs:
            n += 1
            for term in document_vocab:
                t = df[term] if term in df else d
                df[term] = t + 1
        idf = dict()
        for term, f in df.items():
            idf[term] = math.log(n / f) + a
        return idf

    @staticmethod
    def tfidf(tf: Dict[str, float], idf: Dict[str, float]) -> Dict[str, float]:
        tf_idf = dict()
        for term, tf_val in tf.items():
            tf_val = tf_val if bool(tf_val) else 1
            idf_val = idf[term] if term in idf else 1
            # TF-IDF=TF*IDF
            tf_idf[term] = tf_val * idf_val
        return tf_idf
