from statistics import mean

from school.grade import Grade
from school.semester import Semester

class Subject():
    def __init__(self, name:str, full_year:bool=True, weight:float=1.000):
        self.name = name
        self._full_year = full_year
        self.credit = 1.000 if full_year else 0.500
        self._weight = weight

        self.sem1 = Semester(weight=weight)
        self.sem2 = Semester(weight=weight)

        self.mp = {
            1: self.sem1.mp1,
            2: self.sem1.mp2,
            3: self.sem2.mp1,
            4: self.sem2.mp2
        }

    def __str__(self):
        return self.name

    @property
    def final(self):
        if self._full_year:
            sem_avg = (self.sem1.final + self.sem2.final) / 2
        else:
            try:
                sem_avg = self.sem1.final
            except TypeError:
                sem_avg = self.sem2.final
        grade = round(sem_avg + 0.001, 2)
        return Grade(grade=grade, weight=self._weight)

    @property
    def passed(self) -> bool:
        # Corona Virus Canceled one of the exams
        # if self.sem1.exam == None:
        #     if self.sem2.exam != None: return None
        # if self.sem2.exam == None:
        #     if self.sem1.exam != None: return None
        try:
            return self.final.unweighted >= 60
        except TypeError:
            return None

    @classmethod
    def half_year(cls, name:str):
        return cls(name=name, weight=1.000/2, full_year=False)

    @classmethod
    def half_year_honors(cls, name:str):
        return cls(name=name, weight=1.050/2, full_year=False)

    @classmethod
    def half_year_advanced_placement(cls, name:str):
        return cls(name=name, weight=1.100/2, full_year=False)

    @classmethod
    def half_year_international_baccalaureate(cls, name:str):
        return cls(name=name, weight=1.100/2, full_year=False)

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