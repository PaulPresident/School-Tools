import unittest

from school.report_card import ReportCard
from school.marking_period import MarkingPeriod
from school.subject import Subject

class ReportCardTest(unittest.TestCase):
    def setUp(self):
        self.subjects = [
            Subject.honors(name='H English 10', grade=95.55),
            Subject.advanced_placement(name='AP Modern World History', grade=78.24),
            Subject.college_prep(name='CP Geometry', grade=88.99),
            Subject.honors(name='H Biology', grade=92.49)
        ]

        self.marking_periods = [
            MarkingPeriod.mp1(subjects=self.subjects)
        ]

    def test_has_attributes(self):
        report_card = ReportCard(marking_periods=self.marking_periods)

        self.assertEqual(str(report_card.last_marking_period), '1')
        self.assertEqual(report_card.subjects, self.subjects)

    def test_formats_name_to_have_30_characters(self):
        subject = Subject.honors(name='H English 10', grade=94.34)

        self.assertEqual(
            ReportCard.whitespace_name(subject.name),
            'H English 10                  '
        )

    def test_figures_out_earned_honor_roll(self):
        subjects = [
            Subject.honors(name='H English 10', grade=95.55),
            Subject.honors(name='H Biology', grade=92.49)
        ]

        marking_periods = [
            MarkingPeriod.mp1(subjects=subjects)
        ]

        report_card = ReportCard(marking_periods=marking_periods)

        self.assertEqual(
            report_card._honor_roll(),
            'Second Honor Roll'
        )

    def test_report_card_string_representation(self):
        report_card = ReportCard(marking_periods=self.marking_periods)

        self.assertEqual(
            str(report_card),
            '''
____________________________________________
|   Classes                        Grade   |
|   H English 10                      96   |
|   AP Modern World History           78   |
|   CP Geometry                       89   |
|   H Biology                         92   |
____________________________________________



MP1 NGA: 93.050
'''
        )