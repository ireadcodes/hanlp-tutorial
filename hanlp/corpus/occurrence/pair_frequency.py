from hanlp.corpus.occurrence.term_frequency import TermFrequency


class PairFrequency(TermFrequency):
    def __init__(self, term):
        super().__init__(term)
        self.first = ''
        self.second = ''
        self.delimiter = ''
        # 互信息值
        self.mi = 0
        # 左信息熵
        self.le = 0
        # 右信息熵
        self.re = 0
        # 分数
        self.score = 0

    @classmethod
    def create_pair(cls, first, delimiter, second):
        pair_frequency = PairFrequency(first + delimiter + second)
        pair_frequency.first = first
        pair_frequency.delimiter = delimiter
        pair_frequency.second = second
        return pair_frequency
