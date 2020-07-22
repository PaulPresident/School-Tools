from dataclasses import dataclass

from school.subject import Subject

@dataclass
class GradeYear:
    year: int
    subjects: list = []

    @property
    def subjects(self):
        return self.subjects

    def extend_subjects(self, subjects:list):
        for subject in self.subjects:
            if not isinstance(subject, Subject):
                raise TypeError(f'{subject} is not an object of the Subject Class.')
        self.subjects.extend(subjects)

    def remove_subject(self, remove:Subject):
        for subject in self.subjects:
            if subject.name == remove:
                self.subjects.remove(subject)
                return
        raise LookupError(f'{remove} was not found in the list of subjects.')