class Subject():
    TYPES = {
        'CP': 1.000,         'College Prep': 1.000,
        'H': 1.050,          'Honors': 1.050,
        'AP': 1.100,          'Advanced Placement': 1.100,
        'IB': 1.100,          'International Baccalaureate': 1.100,
    }

    def __init__(self, name, grade, type=None):
        self.name = name
        self._name = name[:]
        self._type = type
        self._weight = self.TYPES.get(type, 1.000)
        self._grade = grade

    def __str__(self):
        return self.name

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
        return round(self.grade * self._weight, 3)