class ReportCard():
    def __init__(self, subjects, marking_period=1):
        self._subjects = subjects
        self._marking_period = f'MP{marking_period}'

    def unweighted_nga(self, classes:int):
        return round(sum([subject.grade for subject in self._subjects]) / classes, 3)

    def weighted_nga(self, classes:int):
        return round(sum([subject.weighted_grade for subject in self._subjects]) / classes, 3)

    def _honor_roll(self):
        sum_of_gpa = sum([subject.gpa for subject in self._subjects])
        avg_gpa = sum_of_gpa / len(self._subjects)

        if avg_gpa >= 3.75:
            return 'First Honor Roll'
        if avg_gpa >= 3.50:
            return 'Second Honor Roll'
        return None

    def __str__(self):
        border = '\n____________________________________________\n'
        report_card = border + '|   Classes                        Grade   |\n'
        for subject in self._subjects:
            report_card += f'|   {subject.whitespace_name}    {subject.grade}   |\n'
        report_card += border + f'\n\nCongratulations on achieving {self._honor_roll()}' if self._honor_roll() else border + '\n\n\n'
        report_card += f'{self._marking_period} NGA: {self.weighted_nga(4):.3f}\n'

        return report_card