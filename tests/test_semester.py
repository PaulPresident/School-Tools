import unittest
from unittest.mock import MagicMock

from school.semester import Semester
from school.marking_period import MarkingPeriod

class SemesterTest(unittest.TestCase):
    def test_takes_weight_sets_to_1_if_not_provided_creates_mp1_and_mp2_and_takes_exam_sets_to_none_if_not_provided(self):
        semester = Semester()

        self.assertEqual(semester._weight, 1.000)
        self.assertIsInstance(semester.mp1, MarkingPeriod)
        self.assertIsInstance(semester.mp2, MarkingPeriod)
        self.assertEqual(semester.exam, None)

    def test_allows_for_updating_exam(self):
        semester = Semester()
        semester.exam = 94

        self.assertEqual(semester.exam, 94)

    def test_calculates_final_grade(self):
        mock_mp1 = MagicMock(grade=90)
        mock_mp2 = MagicMock(grade=91)

        semester = Semester(mp1=mock_mp1, mp2=mock_mp2)
        semester.exam = 92

        self.assertEqual(semester.final, 91)


    # def setUp(self):
    #     self.english = Subject(name='English', grade=91)
    #     self.mock_marking_period1 = MagicMock()
    #     self.mock_marking_period2 = MagicMock()
    #     self.mock_marking_period2.subjects = [self.english]
    #     self.marking_periods = (self.mock_marking_period1, self.mock_marking_period2)

    # def test_has_marking_period_1_and_marking_period_2(self):
    #     semester = Semester(marking_periods=self.marking_periods)

    #     self.assertEqual(semester.marking_period1, self.mock_marking_period1)
    #     self.assertEqual(semester.marking_period2, self.mock_marking_period2)

    # def test_adds_exam_score_to_subject_objects(self):
    #     semester = Semester(marking_periods=self.marking_periods)
    #     semester._add_exam_score(exam=('English', 87), exam_type='midterm')

    #     self.assertEqual(self.english.exams['midterm'], 87)

    # def test_has_class_methods_for_each_semester_which_also_adds_exam_scores_to_each_subject(self):
    #     midterm_exams = {'English': 87}
    #     semester = Semester.semester1(marking_periods=self.marking_periods, midterm_exams=midterm_exams)

    #     self.assertEqual(semester.marking_period1, self.mock_marking_period1)
    #     self.assertEqual(semester.marking_period2, self.mock_marking_period2)
    #     self.assertEqual(self.english.exams['midterm'], 87)
