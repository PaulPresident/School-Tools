from typing import List

from school.subject import Subject

class Year():
    def __init__(self, year:int):
        self.year = year
        self._subjects = []

    @property
    def subjects(self) -> list:
        return self._subjects

    def extend_subjects(self, subjects:List[Subject]):
        self._subjects.extend(subjects)

    def remove_subject(self, remove:str):
        for subject in self.subjects:
            if subject.name == remove:
                self._subjects.remove(subject)
                return
        raise LookupError(f'{remove} was not found in the list of subjects.')

    @property
    def completed(self):
        for subject in self.subjects:
            if subject.passed == None:
                return False
        return True

    @property
    def credits(self):
        return sum(subject.credit for subject in self._subjects)

    @property
    def credits_earned(self):
        return sum(
            subject.credit
            for subject in self._subjects
            if subject.passed
        )

    @property
    def unweighted_nga(self):
        grades = [subject.final.unweighted for subject in self._subjects]
        return round(sum(grades) / len(self._subjects), 3)

    @property
    def weighted_nga(self):
        grades = [subject.final.weighted for subject in self._subjects]
        return round(sum(grades) / self.credits, 3)

    @property
    def unweighted_gpa(self):
        gpas = [subject.final.unweighted_gpa for subject in self._subjects]
        return round(sum(gpas) / len(self._subjects), 3)

    @property
    def weighted_gpa(self):
        gpas = [subject.final.weighted_gpa for subject in self._subjects]
        return round(sum(gpas) / len(self._subjects), 3)
