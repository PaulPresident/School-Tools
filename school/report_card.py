class ReportCard():
    def __init__(self, subjects, marking_period=1):
        self._subjects = subjects
        self._marking_period = f'MP{marking_period}'

    def unweighted_nga(self, classes:int):
        return round(sum([subject.grade for subject in self._subjects]) / classes, 3)

    def weighted_nga(self, classes:int):
        return round(sum([subject.weighted_grade for subject in self._subjects]) / classes, 3)

    # def honor_roll(self):
    #     {}

    def __str__(self):
        border = '__________________________________________________________\n'
        report_card = border + '|   Classes                        Grade   |\n'
        for subject in self._subjects:
            report_card += f'|   {subject.whitespace_name}    {subject.grade}   |\n'
        report_card += border + f'\n{self._marking_period} NGA: {self.weighted_nga(4):.3f}\n'

        return report_card