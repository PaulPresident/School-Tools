import unittest

from school.student import Student
from school.year import Year
from school.report_card import ReportCard
from school.transcript import Transcript

class StudentTest(unittest.TestCase):
    def test_has_name(self):
        student = Student(name='Paul')
        self.assertEqual(student.name, 'Paul')

    def test_has_attributes_year_mp_and_highschool(self):
        student = Student(name='Barley')

        self.assertEqual(student._year, 0)
        self.assertEqual(student._mp, 0)
        self.assertIsInstance(student.high_school[9], Year)
        self.assertIsInstance(student.high_school[10], Year)
        self.assertIsInstance(student.high_school[11], Year)
        self.assertIsInstance(student.high_school[12], Year)

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

    def test_updates_year(self):
        student = Student(name='Pacman')
        student.year = 10

        self.assertEqual(student.year, 10)

    def test_year_raises_type_error_If_not_int(self):
        student = Student(name='Raccoon')
        with self.assertRaises(TypeError):
            student.year = '10th Grade'

    def test_year_raises_value_error_if_not_between_9_and_12(self):
        student = Student(name='Grater')
        with self.assertRaises(ValueError):
            student.year = 8

    def test_creates_report_card(self):
        student = Student(name='Cornelius')
        student.year = 10
        student.mp = 2

        self.assertIsInstance(student.report_card(year=9, mp=4), ReportCard)

    def test_raises_value_error_if_requesting_an_unavailable_report_card(self):
        student = Student(name='MeatMan')
        student.year = 10
        student.mp = 3

        with self.assertRaises(ValueError):
            student.report_card(year=11, mp=1)
            student.report_card(year=10, mp=4)

    def test_creates_transcript(self):
        student = Student(name='Chris')
        student.year = 10

        self.assertIsInstance(student.transcript(10), Transcript)

    def test_raises_value_error_if_requesting_an_unavailable_transcript(self):
        student = Student(name='Robert U Gene GayLord')
        student.year = 10

        with self.assertRaises(ValueError):
            student.transcript(year=11)