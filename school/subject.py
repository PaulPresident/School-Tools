class Subject():
    LETTER_GRADES = {
        'A+': (97, 101),      'A': (93, 97),        'A-': (90, 93),
        'B+': (87, 90),       'B': (83, 87),        'B-': (80, 83),
        'C+': (77, 80),       'C': (73, 77),        'C-': (70, 73),
        'D+': (67, 70),       'D': (63, 67),        'D-': (60, 63),
        'F': (0, 60)
    }

    GPA_POINTS = {
        'A+': 4.00,         'A': 3.67,          'A-': 3.67,
        'B+': 3.33,         'B': 3.00,          'B-': 2.67,
        'C+': 2.33,         'C': 2.00,          'C-': 1.67,
        'D+': 1.33,         'D': 1.00,          'D-': 0.67,
        'F': 0.00
    }

    def __init__(self, name:str, grade:float, full_year:bool=True, weight:float=1.000):
        self._name = name
        self._name = name[:]
        self.full_year = full_year
        self.weight = weight
        self._grade = grade

    def __str__(self):
        return self._name

    @property
    def whitespace_name(self):
        while len(self._name) < 30:
            self._name += ' '
        return self._name

    @property
    def grade(self):
        return round(self._grade)

    @property
    def weighted_grade(self):
        return round(self.grade * self.weight, 3)

    def letter_grade(self, grade):
        for letter_grade, limit in self.LETTER_GRADES.items():
            if limit[0] < grade < limit[1]:
                return letter_grade

    @property
    def gpa(self):
        return self.GPA_POINTS.get(self.letter_grade(self.grade))

    @property
    def weighted_gpa(self):
        return self.GPA_POINTS.get(self.letter_grade(self.weighted_grade))



    @classmethod
    def elective(cls, name:str, grade:float):
        return cls(name=name, grade=grade, weight=0.500, full_year=False)

    @classmethod
    def language(cls, name:str, grade:float):
        return cls(name=name, grade=grade)

    @classmethod
    def college_prep(cls, name:str, grade:float):
        return cls(name=name, grade=grade)

    @classmethod
    def honors(cls, name:str, grade:float):
        return cls(name=name, grade=grade, weight=1.050)

    @classmethod
    def advanced_placement(cls, name:str, grade:float):
        return cls(name=name, grade=grade, weight=1.100)

    @classmethod
    def international_baccalaureate(cls, name:str, grade:float):
        return cls(name=name, grade=grade, weight=1.100)