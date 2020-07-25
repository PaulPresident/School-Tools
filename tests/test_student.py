import unittest

from school.student import Student
from school.year import Year

class StudentTest(unittest.TestCase):
    def test_has_name(self):
        student = Student(name='Paul')
        self.assertEqual(student.name, 'Paul')

    def test_has_attributes_year_mp_and_highschool(self):
        student = Student(name='Barley')

        self.assertEqual(student._year, 0)
        self.assertEqual(student._mp, 0)
        self.assertIsNone(student.high_school[9])
        self.assertIsNone(student.high_school[10])
        self.assertIsNone(student.high_school[11])
        self.assertIsNone(student.high_school[12])

    def test_updates_mp(self):
        student = Student(name='Cumin')
        student.mp = 3

        self.assertEqual(student.mp, 3)

    def test_mp_raises_type_error_if_not_int(self):
        student = Student(name='Porter')

        with self.assertRaises(TypeError):
            student.mp = 'mp4'

    def test_mp_raises_value_error_if_greater_than_4(self):
        student = Student(name='Kyle')

        with self.assertRaises(ValueError):
            student.mp = 5

    def test_updates_year_and_creates_year_objects_accordingly(self):
        student = Student(name='Pacman')
        student.year = 9
        year9 = student.high_school[9]
        student.year = 10

        self.assertEqual(student.year, 10)
        self.assertIs(student.high_school[9], year9)
        self.assertIsInstance(student.high_school[10], Year)
        self.assertIsNone(student.high_school[11])

    def test_year_raises_type_error_If_not_int(self):
        student = Student(name='Raccoon')
        with self.assertRaises(TypeError):
            student.year = '10th Grade'

    def test_year_raises_value_error_if_not_between_9_and_12(self):
        student = Student(name='Grater')
        with self.assertRaises(ValueError):
            student.year = 8

    def test_year_raises_value_error_if_less_than_previously_recorded_year(self):
        student = Student(name='Scooter')
        student.year = 11
        with self.assertRaises(ValueError):
            student.year = 9





