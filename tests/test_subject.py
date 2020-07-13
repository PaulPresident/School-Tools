import unittest

from school.subject import Subject

class SubjectTest(unittest.TestCase):
    def test_has_name_and_grade(self):
        subject = Subject(name='H English 10', grade=94.34)

        self.assertEqual(subject.name, 'H English 10')
        self.assertEqual(subject._grade, 94.34)

    def test_has_string_representation(self):
        subject = Subject(name='H Geometry', grade=97.56)

        self.assertEqual(str(subject),'H Geometry')

    def test_has_class_methods_for_determining_subject_type_and_weight(self):
        subject = Subject.advanced_placement(name='AP Modern World History', grade=92.49)

        self.assertEqual(subject.full_year, True)
        self.assertEqual(subject._weight, 1.100)

    def test_has_public_properties_grade_and_weighted_grade(self):
        subject = Subject.international_baccalaureate(name='IB Math Year 1', grade=93.87)

        self.assertEqual(subject.grade, 94)
        self.assertEqual(subject.weighted_grade, 103.400)

    def test_figures_out_letter_grade_from_given_grade(self):
        subject = Subject.international_baccalaureate(name='IB Math Year 1', grade=93.87)

        self.assertEqual(subject.letter_grade(subject.grade), 'A')

    def test_figures_out_gpa_and_weighted_gpa(self):
        subject = Subject.honors(name='H Algebra 2', grade=86.42)

        self.assertEqual(subject.gpa(subject.grade), 3.00)
        self.assertEqual(subject.gpa(subject.weighted_grade), 3.67)


    def test_adds_midterm_exam_score_which_is_also_a_public_property(self):
        subject = Subject(name='CP Physical Science', grade=85.63)
        subject.midterm_exam = 87

        self.assertEqual(subject.exams['midterm'], 87)

    def test_raises_value_error_if_score_is_not_an_integer(self):
        subject = Subject(name='CP Physical Science', grade=85.63)

        with self.assertRaises(ValueError):
            subject.midterm_exam = 87.49

    def test_adds_final_exam_score_which_is_also_a_public_property(self):
        subject = Subject(name='CP Physical Science', grade=85.63)
        subject.final_exam = 91

        self.assertEqual(subject.exams['final'], 91)

    def test_raises_value_error_if_score_is_not_an_integer(self):
        subject = Subject(name='CP Physical Science', grade=85.63)

        with self.assertRaises(ValueError):
            subject.final_exam = 91.52
