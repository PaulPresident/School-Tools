import unittest
from unittest.mock import MagicMock

from school.year import Year
from school.subject import Subject
from school.grade import Grade

class YearTest(unittest.TestCase):
    def setUp(self):
        spanish = MagicMock(credit=1, final=Grade(grade=92.00), passed=True)
        ap_english = MagicMock(credit=1, final=Grade(grade=95.00, weight=1.1), passed=True)
        h_math = MagicMock(credit=1, final=Grade(grade=97.00, weight=1.05), passed=True)

        self.subjects = [spanish, ap_english, h_math]

    def test_has_year_and_subjects_list(self):
        year = Year(year=9)

        self.assertEqual(year.year, 9)
        self.assertEqual(year.subjects, [])

    def test_can_extend_the_list_of_subjects(self):
        subject = Subject('English')

        year = Year(year=10)
        year.extend_subjects(subjects=[subject])

        self.assertEqual(year.subjects, [subject])

    def test_can_remove_a_subject_from_the_list_of_subjects(self):
        year = Year(year=11)
        year.extend_subjects(subjects=[Subject('Math')])
        year.remove_subject(remove='Math')

        self.assertEqual(year.subjects, [])

    def test_remove_subject_raises_lookup_error_if_name_that_does_not_exist_in_subjects_list(self):
        year = Year(year=11)

        with self.assertRaises(LookupError):
            year.remove_subject('Math')

    def test_knows_when_year_is_completed(self):
        year = Year(year=9)
        year.extend_subjects(subjects=[MagicMock(passed=True), MagicMock(passed=False)])

        self.assertEqual(year.completed, True)

    def test_knows_when_year_is_not_completed(self):
        year = Year(year=9)
        year.extend_subjects(subjects=[MagicMock(passed=True), MagicMock(passed=None)])

        self.assertEqual(year.completed, False)

    def test_figures_out_credits_earned_out_of_total_credits(self):
        year = Year(year=9)
        year.extend_subjects(subjects=self.subjects)
        year.extend_subjects(subjects=[MagicMock(credit=1, final=Grade(grade=49.26), passed=False)])

        self.assertEqual(year.credits, 4)
        self.assertEqual(year.credits_earned, 3)

    def test_calculates_unweighted_and_weighted_nga(self):
        year = Year(year=9)
        year.extend_subjects(subjects=self.subjects)

        self.assertEqual(year.unweighted_nga, 94.667)
        self.assertEqual(year.weighted_nga, 99.450)

    def test_has_unweighted_and_weighted_gpa(self):
        year = Year(year=9)
        year.extend_subjects(subjects=self.subjects)

        self.assertEqual(year.unweighted_gpa, 3.780)
        self.assertEqual(year.weighted_gpa, 4.280)