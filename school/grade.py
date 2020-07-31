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

    def __init__(self, grade:float=None, weight:float=1.000):
        if not isinstance(grade, (float, type(None))): raise ValueError('Grade has to be a Float with 2 decimal places!')
        if not isinstance(weight, float): raise ValueError('Weight has to be a Float with 3 decimal places!')
        self._grade = grade
        self._weight = weight

    @property
    def unweighted(self):
        return round(self._grade + 0.001)

    @property
    def weighted(self):
        return round((self.unweighted * self._weight), 3)

    @unweighted.setter
    def unweighted(self, grade):
        if not isinstance(grade, float): raise ValueError('Grade has to be a Float with 2 decimal places!')
        self._grade = grade

    def letter_grade(self, grade):
        for letter_grade, limit in self.LETTER_GRADES.items():
            if limit[0] > grade >= limit[1]:
                return letter_grade

    @property
    def unweighted_gpa(self):
        return self.GPA_POINTS.get(self.letter_grade(self.unweighted))

    @property
    def weighted_gpa(self):
        if self._weight < 1:
            return self.unweighted_gpa
            gpa_weight =(self._weight % 1) * 10
        return round(self.unweighted_gpa + gpa_weight, 3)