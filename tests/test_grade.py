import unittest

from school.grade import Grade

class GradeTest(unittest.TestCase):
    def test_has_grade_and_weight(self):
        grade = Grade(grade=97.56, weight=1.050)

        self.assertEqual(grade._grade, 97.56)
        self.assertEqual(grade._weight, 1.050)

    def test_raises_value_error_if_grade_is_not_a_float_with_two_decimal_places(self):
        with self.assertRaises(ValueError):
            grade = Grade(grade=94)

    def test_raises_value_error_if_weight_is_not_a_float_with_three_decimal_places(self):
        with self.assertRaises(ValueError):
            grade = Grade(grade=94.84, weight=1)

    def test_has_public_properties_grade_and_weighted_grade(self):
        grade = Grade(grade=93.87, weight=1.1)

        self.assertEqual(grade.grade, 94)
        self.assertEqual(grade.weighted_grade, 103)

    def test_allows_for_updating_grade(self):
        grade = Grade(grade=93.87)
        grade.grade = 87.47

        self.assertEqual(grade.grade, 87)

    def test_figures_out_letter_grade_from_given_grade(self):
        grade = Grade(grade=93.87, weight=1.050)

        self.assertEqual(grade.letter_grade(grade.grade), 'A')
        self.assertEqual(grade.letter_grade(grade.weighted_grade), 'A+')

    def test_figures_out_gpa_and_weighted_gpa(self):
        grade = Grade(grade=86.42, weight=1.050)

        self.assertEqual(grade.gpa(grade.grade), 3.00)
        self.assertEqual(grade.gpa(grade.weighted_grade), 3.67)