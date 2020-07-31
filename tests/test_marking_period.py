import unittest

from school.marking_period import MarkingPeriod
from school.grade import Grade

class MarkingPeriodTest(unittest.TestCase):
    def test_creates_grade_object_upon_instantiation(self):
        marking_period = MarkingPeriod()

        self.assertIsInstance(marking_period._grade, Grade)

    def test_allows_for_updating_grade(self):
        marking_period = MarkingPeriod(weight=1.050)
        marking_period.grade = 94.39

        self.assertEqual(marking_period.grade.unweighted, 94)
        self.assertEqual(marking_period.grade.weighted, 98.7)