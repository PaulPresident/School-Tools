class ReportCard():
    def __init__(self, marking_periods:list, semesters:tuple=(None, None)):
        # self.semester1, self.semester2 = semesters
        self.marking_periods = marking_periods
        self.last_marking_period = self.marking_periods[-1]
        self.subjects = self.marking_periods[-1].subjects

    @staticmethod
    def whitespace_name(name):
        while len(name) < 30:
            name += ' '
        return name

    def _honor_roll(self):
        sum_of_gpa = sum([subject.gpa(subject.grade) for subject in self.subjects])
        avg_gpa = sum_of_gpa / len(self.subjects)

        if avg_gpa >= 3.75:
            return 'First Honor Roll'
        if avg_gpa >= 3.50:
            return 'Second Honor Roll'
        return None

    def __str__(self):
        border = '____________________________________________\n'
        report_card = f'\n{border}|   Classes                        Grade   |\n'
        for subject in self.subjects:
            report_card += f'|   {self.whitespace_name(subject.name)}    {subject.grade}   |\n'
        report_card += border + f'\n\nCongratulations on achieving {self._honor_roll()}' if self._honor_roll() else border + '\n\n\n'
        report_card += f'MP{str(self.last_marking_period)} NGA: {self.last_marking_period.weighted_nga:.3f}\n'

        return report_card