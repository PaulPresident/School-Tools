from dataclasses import dataclass

from school.grade import Grade

@dataclass
class MarkingPeriod:
    _weight: float = 1.000
    _grade: Grade = Grade(weight=_weight)

    @property
    def grade(self):
        return self._grade.grade

    @property
    def weighted_grade(self):
        return self._grade.weighted_grade

    @grade.setter
    def grade(self, grade:float):
        self._grade.grade = grade