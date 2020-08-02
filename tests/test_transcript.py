import unittest
from unittest.mock import MagicMock

from school.transcript import Transcript
from school.year import Year
from school.grade import Grade

class TranscriptTest(unittest.TestCase):
    def setUp(self):
        python = MagicMock(credit=0.500, final=Grade(grade=98.07, weight=0.500), passed=True)
        python.name = 'python'
        history = MagicMock(name='history', credit=1.000, final=Grade(grade=92.71, weight=1.100), passed=True)
        history.name = 'history'
        science = MagicMock(name='science', credit=1.000, final=Grade(grade=55.89, weight=1.000), passed=False)
        science.name = 'science'
        gym = MagicMock(name='gym', credit=0.500, final=Grade(grade=99.02, weight=0.500), passed=True)
        gym.name = 'gym'
        english = MagicMock(name='english', credit=1.000, final=Grade(grade=94.30, weight=1.050), passed=True)
        english.name = 'english'
        math = MagicMock(name='math', credit=1.000, final=Grade(grade=98.63, weight=1.050), passed=True)
        math.name = 'math'

        self.subjects9 = [
            python,
            history,
            science
        ]

        self.subjects10 = [
            gym,
            english,
            math
        ]

        self.year9 = Year(year=9)
        self.year9.extend_subjects(subjects=self.subjects9)
        self.year10 = Year(year=10)
        self.year10.extend_subjects(subjects=self.subjects10)

        self.years = [self.year9, self.year10]

    def test_takes_years_and_creates_attributes(self):
        transcript = Transcript(years=self.years)

        self.assertEqual(transcript._years, self.years)
        self.assertEqual(transcript._subjects, self.subjects9 + self.subjects10)

    def test_figures_out_credtis_earned_out_of_total_credits(self):
        transcript = Transcript(years=self.years)

        self.assertEqual(transcript.credits, 5)
        self.assertEqual(transcript.credits_earned, 4)

    def test_calculates_unweighted_and_weighted_nga(self):
        transcript = Transcript(years=self.years)

        self.assertEqual(transcript.unweighted_nga, 89.833)
        self.assertEqual(transcript.weighted_nga, 91.89)

    def test_calculates_unweighted_and_weighted_gpa(self):
        transcript = Transcript(years=self.years)

        self.assertEqual(transcript.unweighted_gpa, 3.223)
        self.assertEqual(transcript.weighted_gpa, 3.557)

    def test_writes_transcript(self):
        transcript = Transcript(years=self.years)

        transcript._test_write()