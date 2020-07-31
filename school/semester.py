from school.marking_period import MarkingPeriod

class Semester():
    def __init__(self, weight:int=1.000, full_year:bool=True):
        self._weight = weight
        self.mp1 = MarkingPeriod(weight)
        self.mp2 = MarkingPeriod(weight)
        self._exam = None

    @property
    def exam(self):
        return self._exam

    @exam.setter
    def exam(self, score):
        self._exam = score

    @property
    def final(self):
        try:
            final = (self.mp1.grade.unweighted * .4) + (self.mp2.grade.unweighted * .4) + (self.exam * .2)
            return round(final + 0.001)
        except TypeError:
            final = (self.mp1.grade.unweighted + self.mp2.grade.unweighted) / 2
            return round(final + .001)