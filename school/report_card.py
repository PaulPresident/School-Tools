from openpyxl import load_workbook
from school.year import Year

# TODO refine (dict and list cuz in calc we use the keys maybe better way?)'
# NOTE change what rc object should know e.g. subjects in mp
# NOTE subject_grades need? could we substitute with just list of grades
class ReportCard():
    def __init__(self, mp:int, year:Year):
        self._mp = mp
        self._year = year
        self._subjects = [subject for subject in self._year.subjects]
        self._subject_grades = {
            subject: subject.mp[self._mp].grade
            for subject in self._subjects
            if subject.mp[self._mp].grade._grade
            }
        self._credits = sum(subject.credit for subject in self._subject_grades.keys())
        self._row = 6

    @property
    def unweighted_nga(self):
        grades = sum(grade.unweighted for grade in self._subject_grades.values())
        return round(grades / len(list(self._subject_grades.keys())), 3)

    @property
    def weighted_nga(self):
        grades = sum(grade.weighted for grade in self._subject_grades.values())
        return round(grades / self._credits, 3)

    @property
    def unweighted_gpa(self):
        gpas = sum(grade.unweighted_gpa for grade in self._subject_grades.values())
        return round(gpas / len(list(self._subject_grades.keys())), 3)

    @property
    def weighted_gpa(self):
        gpas = sum(grade.weighted_gpa for grade in self._subject_grades.values())
        return round(gpas / len(list(self._subject_grades.keys())), 3)

# TODO no subject lower than 80 or 70 in marking period and test
    @property
    def honor_roll(self):
        if self.unweighted_nga >= 93:
            return 'First Honor Roll'
        if self.unweighted_nga >= 83:
            return 'Second Honor Roll'



    def _write_name_and_credits(self, ws, subject):
        self._row += 1
        ws.cell(column=1, row=self._row, value=subject.name)
        ws.cell(column=12, row=self._row, value=subject.credit)

    def _write_grades(self, ws, subject):
        for mp, col in {1:3, 2:4, 3:7, 4:8}.items():
            try:
                ws.cell(column=col, row=self._row, value=subject.mp[mp].grade.unweighted)
            except TypeError:
                continue

# TODO refine
# I don't like these if's and try's research?
    def _write_exams_final_grades(self, ws, subject):
        if subject.sem1.exam:
            ws.cell(column=5, row=self._row, value=subject.sem1.exam)
        if subject.sem2.exam:
            ws.cell(column=9, row=self._row, value=subject.sem2.exam)
        try:
            ws.cell(column=6, row=self._row, value=subject.sem1.final)
        except TypeError: pass
        try:
            ws.cell(column=10, row=self._row, value=subject.sem2.final)
        except TypeError: pass
        try:
            ws.cell(column=11, row=self._row, value=subject.final.unweighted)
        except TypeError: pass

    def write(self):
        wb = load_workbook(filename='Retport Card Template.xlsx')
        ws = wb.active

        for subject in self._subjects:
            self._write_name_and_credits(ws=ws, subject=subject)
            self._write_grades(ws=ws, subject=subject)
            self._write_exams_final_grades(ws=ws, subject=subject)

        ws['A23'] = f'Congratulations on achieving {self.honor_roll}.'
        ws['A24'] = f'MP{self._mp} NGA: {self.weighted_nga}'

        wb.save('Retport Card.xlsx')