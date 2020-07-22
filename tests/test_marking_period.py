import unittest

from school.marking_period import MarkingPeriod
from school.grade import Grade

class MarkingPeriodTest(unittest.TestCase):
    def test_has_grade_set_to_none(self):
        markingperiod = MarkingPeriod()

        self.assertIsInstance(markingperiod._grade, Grade)

    def test_returns_grade_and_weighted_grade(self):
        markingperiod = MarkingPeriod(_grade=Grade(94.39, 1.050))

        self.assertEqual(markingperiod.grade, 94)
        self.assertEqual(markingperiod.weighted_grade, 99)

    def test_allows_for_updating_grade(self):
        markingperiod = MarkingPeriod()
        markingperiod.grade = 92.13

        self.assertEqual(markingperiod.grade, 92)

    # def setUp(self):
    #     self.english = Subject.honors(name='H English 10')
    #     self.english.update_grade(mp='mp1', grade=95.55)

    #     self.history = Subject.advanced_placement(name='AP Modern World History')
    #     self.history.update_grade(mp='mp1', grade=78.24)

    #     self.math = Subject.college_prep(name='CP Geometry')
    #     self.math.update_grade(mp='mp1', grade=88.99)

    #     self.biology = Subject.honors(name='H Biology')
    #     self.biology.update_grade(mp='mp1', grade=92.49)

    #     self.subjects = [
    #         self.english,
    #         self.history,
    #         self.math,
    #         self.biology
    #     ]

    # def test_has_marking_period_number_and_subjects(self):
    #     marking_period = MarkingPeriod(mp='mp1', subjects=self.subjects)

    #     self.assertEqual(marking_period._marking_period, 'mp1')
    #     self.assertEqual(marking_period.subjects, self.subjects)

    # def test_has_string_representation(self):
    #     marking_period = MarkingPeriod(mp='mp1', subjects=self.subjects)

    #     self.assertEqual(str(marking_period), 'mp1')

    # def test_has_class_methods(self):
    #     marking_period = MarkingPeriod.mp1(subjects=self.subjects)

    #     self.assertEqual(marking_period._marking_period, 'mp1')
    #     self.assertEqual(marking_period.subjects, self.subjects)

    # def test_has_dict_attribute_nga_which_stores_unweighted_and_weighted_nga(self):
    #     marking_period = MarkingPeriod.mp1(subjects=self.subjects)

    #     self.assertEqual(marking_period.unweighted_nga, 88.750)
    #     self.assertEqual(marking_period.weighted_nga, 93.050)