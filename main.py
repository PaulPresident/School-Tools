from school.subject import Subject
from school.report_card import ReportCard

subjects = [
    Subject(name='H English 10', grade=95.55, type='H'),
    Subject(name='AP Modern World History', grade=78.24, type='AP'),
    Subject(name='CP Geometry', grade=88.99, type='CP'),
    Subject(name='H Biology', grade=92.49, type='H')
]

report_card = ReportCard(subjects=subjects)

# from main import subjects, report_card
# print(str(report_card))