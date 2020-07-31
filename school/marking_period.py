from school.grade import Grade

class MarkingPeriod():
    def __init__(self, weight:int=1.000):
        self._weight = 1.000
        self._grade = Grade(weight=weight)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade:float):
        self._grade.unweighted = grade