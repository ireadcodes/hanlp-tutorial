import heapq
import math
from collections import defaultdict, deque
from typing import Dict, List, Tuple


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


class TextRankKeyword:
    def __init__(self):
        # 阻尼系数(DampingFactor)，一般取值为0.85
        self.d = 0.85
        # 最大迭代次数
        self.max_iter = 200
        self.min_diff = 0.001

    def get_keywords(self, term_list: List[str], size: int) -> List[Tuple[str, float]]:
        rank_result = self.get_term_and_rank(term_list)
        return heapq.nlargest(size, rank_result.items(), key=lambda item: item[1])

    def get_term_and_rank(self, word_list: List[str]) -> Dict[str, float]:
        # words存储着单词到邻居的映射
        words = defaultdict(set)
        que = deque()
        for w in word_list:
            if w not in words:
                words[w] = set()
            # 保证窗口中只有5个词
            if len(que) >= 5:
                # 移除队首元素
                que.popleft()
            for q_word in que:
                if w == q_word:
                    continue
                # 既然是邻居,那么关系是相互的,遍历一遍即可
                words[w].add(q_word)
                words[q_word].add(w)
            # 将当前单词加入队列
            que.append(w)
        # 初始化每个节点的权重
        score = {key: sigmoid(len(value)) for key, value in words.items()}
        for _ in range(self.max_iter):
            m = dict()
            max_diff = 0
            for key, value in words.items():
                m[key] = 1 - self.d
                # element是key这个词的邻居
                for element in value:
                    size = len(words[element])
                    if key == element or size == 0:
                        continue
                    # 重点：中心词(key)的权重与邻居词的链接总数(size)成反比，与邻居词的权重(score[element])成正比
                    m[key] = m[key] + self.d / size * score.get(element, 0)
                max_diff = max(max_diff, abs(m[key] - score.get(key, 0)))
            # 更新权重
            score = m
            # 算法终止条件为两次迭代间权重最大变化量小于阈值min_diff(权重收敛)，或者总迭代次数达到max_iter
            if max_diff <= self.min_diff:
                break
        return score
