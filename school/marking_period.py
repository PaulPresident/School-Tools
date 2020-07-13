class MarkingPeriod():
    def __init__(self, subjects:list, marking_period:int=None):
        self._marking_period = marking_period
        self.subjects = subjects
        self.nga = {
            'unweighted': self._nga(False),
            'weighted': self._nga(True)
        }

    def __str__(self):
        return str(self._marking_period)

    def _nga(self, is_weighted:bool):
        Credits = sum([1 if subject.full_year else .5 for subject in self.subjects])
        if is_weighted:
            return round(sum([subject.weighted_grade for subject in self.subjects]) / Credits, 3)
        return round(sum([subject.grade for subject in self.subjects]) / Credits, 3)



    @classmethod
    def mp1(cls, subjects):
        return cls(marking_period=1, subjects=subjects)

    @classmethod
    def mp2(cls, subjects):
        return cls(marking_period=2, subjects=subjects)

    @classmethod
    def mp3(cls, subjects):
        return cls(marking_period=3, subjects=subjects)

    @classmethod
    def mp4(cls, subjects):
        return cls(marking_period=4, subjects=subjects)