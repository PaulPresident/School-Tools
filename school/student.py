from school.year import Year

class Student():
    def __init__(self, name:str):
        self.name = name
        self._year = 0
        self._mp = 0
        self.high_school = {
            9: None,        10: None,
            11: None,       12: None,
        }

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, mp:int):
        if not isinstance(mp, int): raise TypeError('Please Provide an Integer!')
        if mp > 4: raise ValueError('Invalid Marking Period: Marking Period cannot exceed 4!')
        self._mp = mp

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, current_year:int):
        if not isinstance(current_year, int): raise TypeError('Please Provide an Integer!')
        if not 9 <= current_year <= 12: raise ValueError('Invlid Year: Only Grades 9-12 are supported!')
        if self._year > current_year: raise ValueError('Invlaid year assignment')
        self._year = current_year
        for year, value in self.high_school.items():
            if not value and year <= current_year:
                self.high_school[year] = Year(year=year)
