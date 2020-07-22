class Grade():
    LETTER_GRADES = {
        'A+': (200, 97),      'A': (97, 93),        'A-': (93, 90),
        'B+': (90, 87),       'B': (87, 83),        'B-': (83, 80),
        'C+': (80, 77),       'C': (77, 73),        'C-': (73, 70),
        'D+': (70, 67),       'D': (67, 63),        'D-': (63, 60),
        'F': (60, 0)
    }

    GPA_POINTS = {
        'A+': 4.00,         'A': 3.67,          'A-': 3.67,
        'B+': 3.33,         'B': 3.00,          'B-': 2.67,
        'C+': 2.33,         'C': 2.00,          'C-': 1.67,
        'D+': 1.33,         'D': 1.00,          'D-': 0.67,
        'F': 0.00
    }

    def __init__(self, grade:float=0.00, weight:float=1.000):
        if not isinstance(grade, float): raise ValueError('Grade has to be a Float with 2 decimal places!')
        if not isinstance(weight, float): raise ValueError('Weight has to be a Float with 3 decimal places!')
        self._grade = grade
        self._weight = weight

    @property
    def grade(self):
        return round(self._grade)

    @property
    def weighted_grade(self):
        return round(self.grade * self._weight)

    @grade.setter
    def grade (self, grade):
        if not isinstance(grade, float): raise ValueError('Grade has to be a Float with 2 decimal places!')
        self._grade = grade

    def letter_grade(self, grade):
        for letter_grade, limit in self.LETTER_GRADES.items():
            if limit[0] > grade >= limit[1]:
                return letter_grade

    def gpa(self, grade):
        return self.GPA_POINTS.get(self.letter_grade(grade))