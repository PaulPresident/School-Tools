from statistics import mean

from school.grade import Grade
from school.semester import Semester

class Subject():
    def __init__(self, name:str, full_year:bool=True, weight:float=1.000):
        self.name = name
        self._full_year = full_year
        self.credit = 1.00 if full_year else 0.50
        self._weight = weight

        self.sem1 = Semester(self._weight)
        self.sem2 = Semester(self._weight)

    def __str__(self):
        return self.name

    @property
    def final(self):
        return round((self.sem1.final + self.sem2.final) / 2)



    @classmethod
    def elective(cls, name:str):
        return cls(name=name, weight=0.500, full_year=False)

    @classmethod
    def language(cls, name:str):
        return cls(name=name)

    @classmethod
    def college_prep(cls, name:str):
        return cls(name=name)

    @classmethod
    def honors(cls, name:str):
        return cls(name=name, weight=1.050)

    @classmethod
    def advanced_placement(cls, name:str):
        return cls(name=name, weight=1.100)

    @classmethod
    def international_baccalaureate(cls, name:str):
        return cls(name=name, weight=1.100)