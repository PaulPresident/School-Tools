import unittest

from school.subject import Subject
from school.semester import Semester
from school.marking_period import MarkingPeriod

class SubjectTest(unittest.TestCase):
    def test_takes_name(self):
        subject = Subject(name='H English 10')

        self.assertEqual(subject.name, 'H English 10')

    def test_has_string_representation(self):
        subject = Subject(name='H Geometry')

        self.assertEqual(str(subject), 'H Geometry')

    def test_has_class_methods_for_determining_subject_type_and_weight(self):
        subject = Subject.advanced_placement(name='AP Modern World History')

        self.assertEqual(subject._full_year, True)
        self.assertEqual(subject._weight, 1.100)

    def test_figures_out_credit_from_subject_type(self):
        subject = Subject.advanced_placement(name='AP Modern World History')
        elective = Subject.half_year(name='Intro to Python')

        self.assertEqual(subject.credit, 1.00)
        self.assertEqual(elective.credit, 0.50)

    def test_creates_sem1_and_sem2_objects(self):
        subject = Subject(name='Intro to Python')

        self.assertIsInstance(subject.sem1, Semester)
        self.assertIsInstance(subject.sem2, Semester)

    def test_makes_marking_period_accessible_by_dictionary(self):
        subject = Subject('H Chemistry')

        self.assertIsInstance(subject.mp[1], MarkingPeriod)
        self.assertIsInstance(subject.mp[2], MarkingPeriod)
        self.assertIsInstance(subject.mp[3], MarkingPeriod)
        self.assertIsInstance(subject.mp[4], MarkingPeriod)

    def test_has_public_property_which_calculates_final_grade_when_subject_is_full_year(self):
        subject = Subject.advanced_placement('AP Chemistry')
        subject.sem1.mp1.grade = 97.52
        subject.sem1.mp2.grade = 93.83
        subject.sem1.exam = 89
        subject.sem2.mp1.grade = 95.29
        subject.sem2.mp2.grade = 87.02
        subject.sem2.exam = 92

        self.assertEqual(subject.final.unweighted, 93)
        self.assertEqual(subject.final.weighted, 102.3)

    def test_has_public_property_which_calculates_final_grade_when_subject_is_not_full_year(self):
        subject = Subject.half_year('CAD1')
        subject.sem2.mp1.grade = 95.02
        subject.sem2.mp2.grade = 98.49

        self.assertEqual(subject.final.unweighted, 97)
        self.assertEqual(subject.final.weighted, 48.5)

    def test_passes_if_final_is_higher_than_60_and_grades_are_complete_with_both_or_neither_of_the_exams(self):
        subject = Subject('AP Chemistry')
        subject.sem1.mp1.grade = 97.52
        subject.sem1.mp2.grade = 93.83
        subject.sem1.exam = 89
        subject.sem2.mp1.grade = 95.29
        subject.sem2.mp2.grade = 87.02
        subject.sem2.exam = 92

        self.assertEqual(subject.passed, True)

    def test_not_passing_if_final_is_lower_than_60(self):
        subject = Subject('AP Chemistry')
        subject.sem1.mp1.grade = 50.00
        subject.sem1.mp2.grade = 50.00
        subject.sem2.mp1.grade = 50.00
        subject.sem2.mp2.grade = 50.00

        self.assertEqual(subject.passed, False)

    def test_passed_is_none_if_grades_are_not_complete(self):
        subject = Subject('AP Chemistry')
        subject.sem1.mp1.grade = 97.52
        subject.sem2.mp1.grade = 95.29
        subject.sem2.mp2.grade = 87.02

        self.assertEqual(subject.passed, None)

# Corona Virus Canceled one of the exams
    # def test_passed_is_none_if_only_one_of_the_exams(self):
    #     subject = Subject('AP Chemistry')
    #     subject.sem1.mp1.grade = 97.52
    #     subject.sem1.mp2.grade = 93.83
    #     subject.sem2.mp1.grade = 95.29
    #     subject.sem2.mp2.grade = 87.02
    #     subject.sem2.exam = 92

    #     self.assertEqual(subject.passed, None)