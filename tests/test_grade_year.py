import unittest

from school.grade_year import GradeYear

class GradeYearTest(unittest.TestCase):
    def test_has_year_and_subjects_list(self):
        grade_year = GradeYear(year=9)

        self.assertEqual(grade_year.year, 9)
        self.assertEqual(grade_year.subjects, [])