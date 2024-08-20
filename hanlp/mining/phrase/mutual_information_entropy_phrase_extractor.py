from typing import List

from hanlp.corpus.occurrence.occurrence import Occurrence


# 利用互信息和左右熵的短语提取器
class MutualInformationEntropyPhraseExtractor:
    def __init__(self):
        pass

    def extract_phrase(self, sentence_list: List[List[str]], size: int) -> List[str]:
        phrase_list = list()
        occurrence = Occurrence()
        for sentence in sentence_list:
            occurrence.add_all(sentence)
        occurrence.compute()
