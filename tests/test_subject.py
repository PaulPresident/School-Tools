import unittest

from school.subject import Subject

class SubjectTest(unittest.TestCase):
    def test_takes_attributes_name_and_type_and_grade(self):
        subject = Subject(name='H English 10', grade=94.34, type='Honors')

        self.assertEqual(
            subject.name,
            'H English 10'
        )

        self.assertEqual(
            subject._type,
            'Honors'
        )

        self.assertEqual(
            subject._grade,
            94.34
        )

    def test_has_name_with_whitespace_characters(self):
        subject = Subject(name='H English 10', grade=94.34, type='Honors')

        self.assertEqual(
            subject.whitespace_name,
            'H English 10                  '
        )

    def test_figures_out_weight_from_type(self):
        subject = Subject(name='AP Calculus BC', grade=89.22, type='AP')

        self.assertEqual(
            subject._weight,
            1.100
        )

    def test_sets_weight_to_1_if_type_attribute_left_empty(self):
        subject = Subject(name='Spanish 4', grade=91.45, type='')

        self.assertEqual(
            subject._weight,
            1.000
        )

    def test_has_string_representation(self):
        subject = Subject(name='H Geometry', grade=97.56, type='H')

        self.assertEqual(
            str(subject),
            'H Geometry'
        )

    def test_has_public_properties_grade_and_weighted_grade(self):
        subject = Subject(name='IB Math Year 1', grade=93.87, type='IB')

        self.assertEqual(
            subject.grade,
            94
        )

        self.assertEqual(
            subject.weighted_grade,
            103.400
        )