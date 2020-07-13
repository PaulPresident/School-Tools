import unittest
from unittest.mock import MagicMock

from school.semester import Semester
from school.subject import Subject

class SemesterTest(unittest.TestCase):
    def setUp(self):
        self.english = Subject(name='English', grade=91)
        self.mock_marking_period1 = MagicMock()
        self.mock_marking_period2 = MagicMock()
        self.mock_marking_period2.subjects = [self.english]
        self.marking_periods = (self.mock_marking_period1, self.mock_marking_period2)

    def test_has_marking_period_1_and_marking_period_2(self):
        semester = Semester(marking_periods=self.marking_periods)

        self.assertEqual(semester.marking_period1, self.mock_marking_period1)
        self.assertEqual(semester.marking_period2, self.mock_marking_period2)

    def test_adds_exam_score_to_subject_objects(self):
        semester = Semester(marking_periods=self.marking_periods)
        semester._add_exam_score(exam=('English', 87), exam_type='midterm')

        self.assertEqual(self.english.exams['midterm'], 87)

    def test_has_class_methods_for_each_semester_which_also_adds_exam_scores_to_each_subject(self):
        midterm_exams = {'English': 87}
        semester = Semester.semester1(marking_periods=self.marking_periods, midterm_exams=midterm_exams)

        self.assertEqual(semester.marking_period1, self.mock_marking_period1)
        self.assertEqual(semester.marking_period2, self.mock_marking_period2)
        self.assertEqual(self.english.exams['midterm'], 87)
