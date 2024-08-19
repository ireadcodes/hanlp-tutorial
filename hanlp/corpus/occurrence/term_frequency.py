class TermFrequency:
    def __init__(self, term, frequency=1):
        self.term = term
        self.frequency = frequency

    def increase_one(self):
        return self.increase(1)

    def increase(self, number):
        self.frequency += number
        return self.frequency
