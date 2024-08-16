from typing import List, Dict

from hanlp.summary.bm25 import BM25


class TextRankSentence:
    def __init__(self, docs: List[List[str]]):
        self.d = 0.85
        self.max_iter = 200
        self.min_diff = 0.001
        # 拆分为[句子[单词]]形式的文档
        self.docs = docs
        # BM25相似度
        self.bm25 = BM25(docs)
        # 文档句子的个数
        self.D = len(docs)
        # 句子和其他句子的相关程度
        self.weight: List[List[float]] = [[0.0 for _ in range(self.D)] for _ in range(self.D)]
        # 该句子和其他句子相关程度之和
        self.weight_sum: List[float] = [0.0 for _ in range(self.D)]
        # 迭代之后收敛的权重，下标表示句子序号，元素表示权重值
        self.vertex: List[float] = [0.0 for _ in range(self.D)]
        # 排序后的最终结果 score <-> index
        self.top: Dict[float, int] = dict()
        self.solve()

    def solve(self):
        cnt = 0
        for sentence in self.docs:
            scores = self.bm25.sim_all(sentence)
            self.weight[cnt] = scores
            # 减掉自己，自己跟自己肯定最相似
            self.weight_sum[cnt] = sum(scores) - scores[cnt]
            self.vertex[cnt] = 1.0
            cnt += 1
        # TextRank核心公式计算
        for _ in range(self.max_iter):
            m = [0.0 for _ in range(self.D)]
            max_diff = 0
            for i in range(self.D):
                m[i] = 1 - self.d
                for j in range(self.D):
                    if j == i or self.weight_sum[j] == 0:
                        continue
                    m[i] += (self.d * self.weight[j][i] / self.weight_sum[j] * self.vertex[j])
                diff = abs(m[i] - self.vertex[i])
                if diff > max_diff:
                    max_diff = diff
            self.vertex = m
            if max_diff < self.min_diff:
                break
        # 排序
        top_temp = dict()
        for i in range(self.D):
            top_temp[self.vertex[i]] = i
        self.top = dict(sorted(top_temp.items(), key=lambda item: item[0], reverse=True))

    def get_top_sentence(self, size: int) -> List[int]:
        values = list(self.top.values())
        size = min(size, len(values))
        return values[: size]
