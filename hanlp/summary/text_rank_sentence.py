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

        assert self.weight == [
            [11.753084407052972, 0.44331163522773204, 0, 0, 0, 1.352416199115756, 0, 0.4117092216273392],
            [0.3035228568201552, 8.33607751710072, 0, 0, 0, 0, 0, 0.4117092216273392],
            [0, 0, 5.235243396719065, 3.5254479239253316, 0.5759367227750868, 0, 0, 0],
            [0, 0, 3.5254479239253316, 4.540540914023763, 1.7934859325053383, 0, 0, 0],
            [0, 0, 0.4801689536300377, 1.495261943728469, 3.8442932447482363, 0, 0, 0],
            [0.6416573207483514, 0, 0, 0, 0, 3.6303898597917135, 0, 0],
            [0, 0, 0, 0, 0, 0, 8.82994128637751, 0.8703668608170706],
            [0.3035228568201552, 0.44331163522773204, 0, 0, 0, 0, 0.9371754045045219, 8.612189346995757]
        ]
        assert self.weight_sum == [2.2074370559708267, 0.7152320784474941, 4.101384646700419, 5.31893385643067,
                                   1.9754308973585069, 0.6416573207483518, 0.8703668608170698, 1.6840098965524088]
        assert self.vertex == [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

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

        assert self.vertex == [1.3152665873775866, 0.6812941175078984, 1.028618664015146, 1.3201165242359068, 0.6512648117489467, 0.8350974523541307, 0.798425569645021, 1.3699162731153676]

        # 排序
        top_temp = dict()
        for i in range(self.D):
            top_temp[self.vertex[i]] = i
        self.top = dict(sorted(top_temp.items(), key=lambda item: item[0], reverse=True))

    def get_top_sentence(self, size: int) -> List[int]:
        values = list(self.top.values())
        size = min(size, len(values))
        return values[: size]
