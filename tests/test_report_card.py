import unittest

from school.report_card import ReportCard
from school.year import Year
from school.subject import Subject

class ReportCardTest(unittest.TestCase):
    def setUp(self):
        python = Subject.half_year(name='Intro to Python')
        history = Subject.advanced_placement(name='AP Modern World History')
        english = Subject.honors(name='H English')
        science = Subject.college_prep(name='CP Biology')
        math = Subject.honors(name='H Geometry')
        spanish = Subject.language(name='Spanish 3')

        python.sem1.mp1.grade = 98.07
        python.sem1.mp2.grade = 99.42
        history.sem1.mp1.grade = 93.71
        history.sem1.mp2.grade = 89.29
        history.sem1.exam = 76
        english.sem1.mp1.grade = 92.30
        english.sem1.mp2.grade = 96.85
        science.sem1.mp1.grade = 95.04
        science.sem1.mp2.grade = 94.95
        math.sem1.mp1.grade = 97.34
        math.sem1.mp2.grade = 99.49
        spanish.sem1.mp1.grade = 91.72
        spanish.sem1.mp2.grade = 91.80

        self.subjects = [
            python,
            history,
            english,
            science,
            math,
            spanish
        ]

        self.year = Year(year=9)
        self.year.extend_subjects(subjects=self.subjects)

    def test_takes_mp_grade_year(self):
        report_card = ReportCard(mp=2, year=self.year)

        self.assertEqual(report_card._mp, 2)
        self.assertIsInstance(report_card._year, Year)

    def test_creates_lists_of_subjects_and_has_total_credits(self):
        report_card = ReportCard(mp=2, year=self.year)

        self.assertEqual(report_card._subjects, self.subjects)
        self.assertEqual(report_card._subjects_in_mp, self.subjects)
        self.assertEqual(report_card._grades, [subject.mp[2].grade for subject in self.subjects])
        self.assertEqual(report_card._credits, 5.5)

    def test_calculates_unweighted_and_weighted_nga(self):
        report_card = ReportCard(mp=2, year=self.year)

        self.assertEqual(report_card.unweighted_nga, 95.167)
        self.assertEqual(report_card.weighted_nga, 98.218)

    def test_calculates_unweighted_and_weighted_gpa(self):
        report_card = ReportCard(mp=2, year=self.year)

        self.assertEqual(report_card.unweighted_gpa, 3.778)
        self.assertEqual(report_card.weighted_gpa, 4.112)

    def test_figures_out_honor_roll(self):
        report_card = ReportCard(mp=2, year=self.year)

        self.assertEqual(report_card.honor_roll, 'First Honor Roll')

    def test_writes_report_card(self):
        report_card = ReportCard(mp=2, year=self.year)

        report_card._test_write()