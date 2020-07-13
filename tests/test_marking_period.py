import unittest

from school.marking_period import MarkingPeriod
from school.subject import Subject

class MarkingPeriodTest(unittest.TestCase):
    def setUp(self):
        self.subjects = [
            Subject.honors(name='H English 10', grade=95.55),
            Subject.advanced_placement(name='AP Modern World History', grade=78.24),
            Subject.college_prep(name='CP Geometry', grade=88.99),
            Subject.honors(name='H Biology', grade=92.49)
        ]

    def test_has_marking_period_number_and_subjects(self):
        marking_period = MarkingPeriod(marking_period=1, subjects=self.subjects)

        self.assertEqual(marking_period._marking_period, 1)
        self.assertEqual(marking_period.subjects, self.subjects)

    def test_has_string_representation(self):
        marking_period = MarkingPeriod(marking_period=1, subjects=self.subjects)

        self.assertEqual(str(marking_period), '1')

    def test_has_class_methods(self):
        marking_period = MarkingPeriod.mp1(subjects=self.subjects)

        self.assertEqual(marking_period._marking_period, 1)
        self.assertEqual(marking_period.subjects, self.subjects)

    def test_has_dict_attribute_nga_which_has_unweighted_and_weighted_nga(self):
        marking_period = MarkingPeriod.mp1(subjects=self.subjects)

        self.assertEqual(marking_period.nga['unweighted'], 88.750)
        self.assertEqual(marking_period.nga['weighted'], 93.050)