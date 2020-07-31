import unittest

from school.semester import Semester
from school.marking_period import MarkingPeriod

class SemesterTest(unittest.TestCase):
    def test_takes_weight_and_full_year_creates_mp1_and_mp2_and_sets_exam_to_none(self):
        semester = Semester()

        self.assertEqual(semester._weight, 1.000)
        self.assertIsInstance(semester.mp1, MarkingPeriod)
        self.assertIsInstance(semester.mp2, MarkingPeriod)
        self.assertEqual(semester.exam, None)

    def test_allows_for_updating_exam(self):
        semester = Semester()
        semester.exam = 94

        self.assertEqual(semester.exam, 94)

    def test_calculates_final_grade_with_exam(self):
        semester = Semester()
        semester.mp1.grade = 90.13
        semester.mp2.grade = 95.29
        semester.exam = 92

        self.assertEqual(semester.final, 92)

    def test_calculates_final_grade_without_exam(self):
        semester = Semester()
        semester.mp1.grade = 90.13
        semester.mp2.grade = 95.29

        self.assertEqual(semester.final, 93)