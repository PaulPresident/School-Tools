import unittest

from school.subject import Subject

class SubjectTest(unittest.TestCase):
    def test_has_name_and_grade(self):
        subject = Subject.honors(name='H English 10', grade=94.34)

        self.assertEqual(subject._name, 'H English 10')
        self.assertEqual(subject._grade, 94.34)

# TODO
    # def test_has_class_methods_for_determining_types(self):
    #     pass

    # def test_takes_SubjectType_object_and_unpacks_it_into_full_year_and_weight(self):
    #     subject = Subject.advanced_placement(name='AP Calculus BC', grade=89.22)

    #     self.assertEqual(subject.full_year, True)
    #     self.assertEqual(subject.weight, 1.100)

    def test_has_name_with_whitespace_characters(self):
        subject = Subject.honors(name='H English 10', grade=94.34)

        self.assertEqual(
            subject.whitespace_name,
            'H English 10                  '
        )

    def test_has_string_representation(self):
        subject = Subject.honors(name='H Geometry', grade=97.56)

        self.assertEqual(str(subject),'H Geometry')

    def test_has_public_properties_grade_and_weighted_grade(self):
        subject = Subject.international_baccalaureate(name='IB Math Year 1', grade=93.87)

        self.assertEqual(subject.grade, 94)
        self.assertEqual(subject.weighted_grade, 103.400)

    def test_figures_out_letter_grade_from_given_grade(self):
        subject = Subject.international_baccalaureate(name='IB Math Year 1', grade=93.87)

        self.assertEqual(subject.letter_grade(subject.grade), 'A')

    def test_has_public_properties_gpa_and_weighted_gpa(self):
        subject = Subject.honors(name='H Algebra 2', grade=86.42)

        self.assertEqual(subject.gpa, 3.00)
        self.assertEqual(subject.weighted_gpa, 3.67)