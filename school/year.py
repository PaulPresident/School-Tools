from dataclasses import dataclass, field
from typing import List

from school.subject import Subject

@dataclass
class Year:
    year: int
    _subjects: List[Subject] = field(default_factory=lambda: [])

    @property
    def subjects(self):
        return self._subjects

    def extend_subjects(self, subjects:list):
        for subject in subjects:
            if not isinstance(subject, Subject):
                raise TypeError(f'{subject} is not an object of the Subject Class.')
        self._subjects.extend(subjects)

    def remove_subject(self, remove:str):
        for subject in self.subjects:
            if subject.name == remove:
                self._subjects.remove(subject)
                return
        raise LookupError(f'{remove} was not found in the list of subjects.')