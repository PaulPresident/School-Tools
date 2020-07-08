import unittest

from school.report_card import ReportCard
from school.subject import Subject

class ReportCardTest(unittest.TestCase):
    def setUp(self):
        self.subjects = [
            Subject(name='H English 10', grade=95.55, type='H'),
            Subject(name='AP Modern World History', grade=78.24, type='AP'),
            Subject(name='CP Geometry', grade=88.99, type='CP'),
            Subject(name='H Biology', grade=92.49, type='H')
        ]
    def test_has_attributes(self):
        subjects = [
            Subject(name='Math', grade=100)
        ]
        report_card = ReportCard(subjects=subjects, marking_period=1)

        self.assertEqual(
            report_card._subjects,
            subjects
        )

        self.assertEqual(
            report_card._marking_period,
            'MP1'
        )

    def test_calculates_unweighted_nga(self):
        report_card = ReportCard(subjects=self.subjects, marking_period=1)

        self.assertEqual(
            report_card.unweighted_nga(4),
            88.750
        )

    def test_calculates_weighted_nga(self):
        report_card = ReportCard(subjects=self.subjects, marking_period=1)

        self.assertEqual(
            report_card.weighted_nga(4),
            93.050
        )


    def test_report_card_string_representation(self):
        report_card = ReportCard(subjects=self.subjects, marking_period=1)

        self.assertEqual(
            str(report_card),
            '''__________________________________________________________
|   Classes                        Grade   |
|   H English 10                      96   |
|   AP Modern World History           78   |
|   CP Geometry                       89   |
|   H Biology                         92   |
__________________________________________________________

MP1 NGA: 93.050
'''
        )