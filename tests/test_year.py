import unittest

from school.year import Year
from school.subject import Subject

class GradeYearTest(unittest.TestCase):
    def test_has_year_and_subjects_list(self):
        grade_year = Year(year=9)

        self.assertEqual(grade_year.year, 9)
        self.assertEqual(grade_year.subjects, [])

    def test_can_extend_the_list_of_subjects(self):
        subject = Subject('English')

        grade_year = Year(year=10)
        grade_year.extend_subjects(subjects=[subject])

        self.assertEqual(grade_year.subjects, [subject])

    def test_extend_subjects_raises_value_error_if_not_given_subject_objects(self):
        grade_year = Year(year=10)

        with self.assertRaises(TypeError):
            grade_year.extend_subjects(subjects=['English', 'Math', 'Science'])

    def test_can_remove_a_subject_from_the_list_of_subjects(self):
        grade_year = Year(year=11)
        grade_year.extend_subjects(subjects=[Subject('Math')])
        grade_year.remove_subject(remove='Math')

        self.assertEqual(grade_year.subjects, [])

    def test_remove_subject_raises_lookup_error_if_name_that_does_not_exist_in_subjects_list(self):
        grade_year = Year(year=11)

        with self.assertRaises(LookupError):
            grade_year.remove_subject('Math')