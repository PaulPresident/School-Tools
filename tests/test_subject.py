import unittest

from school.subject import Subject
from school.grade import Grade
from school.semester import Semester

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
        elective = Subject.elective(name='Intro to Python')

        self.assertEqual(subject.credit, 1.00)
        self.assertEqual(elective.credit, 0.50)

    # def test_updates_grade_object_in_grades_list_by_marking_period(self):
    #     subject = Subject(name='H Geometry')
    #     subject.update_grade(mp='mp1', grade=95.60)

    #     self.assertIsInstance(subject._grades['mp1'], Grade)

    # def test_stores_all_grades_in_variables_by_their_mp(self):
    #     subject = Subject(name='H Physical Science')
    #     subject.update_grade(mp='mp1', grade=95.60)
    #     subject.update_grade(mp='mp2', grade=98.29)

    #     self.assertEqual(subject.mp1._grade, 95.60)
    #     self.assertEqual(subject.mp2._grade, 98.29)

    def test_creates_sem1_and_sem2_objects(self):
        subject = Subject(name='Intro to Python')

        self.assertIsInstance(subject.sem1, Semester)
        self.assertIsInstance(subject.sem2, Semester)


    def test_has_public_property_which_calculates_final_grade(self):
        subject = Subject('Honors')

    # def test_adds_midterm_exam_score_which_is_also_a_public_property(self):
    #     subject = Subject(name='CP Physical Science')
    #     subject.midterm_exam = 87

    #     self.assertEqual(subject.exams['midterm'], 87)

    # def test_raises_value_error_if_score_is_not_an_integer(self):
    #     subject = Subject(name='CP Physical Science')

    #     with self.assertRaises(ValueError):
    #         subject.midterm_exam = 87.49

    # def test_adds_final_exam_score_which_is_also_a_public_property(self):
    #     subject = Subject(name='CP Physical Science')
    #     subject.final_exam = 91

    #     self.assertEqual(subject.exams['final'], 91)

    # def test_raises_value_error_if_score_is_not_an_integer(self):
    #     subject = Subject(name='CP Physical Science')

    #     with self.assertRaises(ValueError):
    #         subject.final_exam = 91.52

    # def test_calculates_sem1_grade(self):
    #     subject = Subject('Spanish 3')
    #     subject.update_grade(mp='mp1', grade=93.85)
    #     subject.update_grade(mp='mp2', grade=91.03)
    #     subject.midterm_exam = 89

    #     self.assertEqual(subject.sem1, 92)

    # def test_calculates_final_grade(self):
    #     subject = Subject('Spanish 3')
    #     subject.update_grade(mp='mp1', grade=93.85)
    #     subject.update_grade(mp='mp2', grade=91.03)
    #     subject.update_grade(mp='mp3', grade=90.02)
    #     subject.update_grade(mp='mp4', grade=87.48)
    #     subject.midterm_exam = 89
    #     subject.final_exam = 92

    #     self.assertEqual(subject.sem1, 91)