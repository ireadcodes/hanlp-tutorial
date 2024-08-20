from hanlp.corpus.occurrence.pair_frequency import PairFrequency


class TriaFrequency(PairFrequency):
    def __init__(self, term):
        super().__init__(term)
        self.third = ''

    @classmethod
    def create_trie(cls, first, delimiter, second, third):
        from hanlp.corpus.occurrence.occurrence import RIGHT
        tria_frequency = TriaFrequency(first + delimiter + second + RIGHT + third)
        tria_frequency.first = first
        tria_frequency.second = second
        tria_frequency.third = third
        tria_frequency.delimiter = delimiter
        return tria_frequency
