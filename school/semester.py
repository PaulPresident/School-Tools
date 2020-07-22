from dataclasses import dataclass

from school.marking_period import MarkingPeriod

@dataclass
class Semester:
    _weight: float = 1.000
    mp1: MarkingPeriod = MarkingPeriod(_weight)
    mp2: MarkingPeriod = MarkingPeriod(_weight)
    _exam: int = None

    @property
    def exam(self):
        return self._exam

    @exam.setter
    def exam(self, score):
        self._exam = score

    @property
    def final(self):
        return round((self.mp1.grade * .4) + (self.mp2.grade * .4) + (self.exam * .2))