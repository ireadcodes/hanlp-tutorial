import math


class WordInfo:
    def __init__(self, text):
        # 词语
        self.text = text
        # 左邻接字集合，键是相邻字符，值是[频率]，为啥频率要用数组表示而不是整数型？
        self.left = dict()
        # 右邻接字集合
        self.right = dict()
        # 词频
        self.frequency = 0
        self.p = 0.0
        self.left_entropy = 0.0
        self.right_entropy = 0.0
        # 互信息
        self.aggregation = float("inf")
        # 信息熵
        self.entropy = 0.0

    def __repr__(self):
        return self.text

    def update(self, left_c, right_c):
        self.frequency += 1
        self.increase_frequency(left_c, self.left)
        self.increase_frequency(right_c, self.right)

    def increase_frequency(self, c, storage):
        if c in storage:
            storage[c][0] += 1
        else:
            freq = [1]
            storage[c] = freq

    def compute_probability_entropy(self, length):
        # self.text = '演'
        # self.left = {'\x00': [2], '上': [1], '卫': [2], '国': [1], '教': [4], '至': [1], '躁': [1]}
        # self.right = {'\x00': [1], '义': [1], '军': [1], '回': [1], '士': [2], '抱': [1], '来': [1], '武': [2], '膝': [1], '阵': [1]}
        self.p = self.frequency / length
        self.left_entropy = self.compute_entropy(self.left)
        self.right_entropy = self.compute_entropy(self.right)
        self.entropy = min(self.left_entropy, self.right_entropy)

    def compute_entropy(self, storage):
        res = 0.0
        for value in storage.values():
            # 相邻词的频数除以本词频数
            pp = value[0] / self.frequency
            # 计算信息熵
            res -= pp * math.log(pp)
        return res

    def compute_aggregation(self, word_cands):
        # 单个字
        if len(self.text) == 1:
            self.aggregation = math.sqrt(self.p)
            return
        # 多个字
        for i in range(1, len(self.text)):
            # 互信息计算，为啥这里没用log？
            res = self.p / word_cands[self.text[0:i]].p / word_cands[self.text[i:]].p
            self.aggregation = min(self.aggregation, res)
