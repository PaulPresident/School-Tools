class Semester():
    def __init__(self, marking_periods:tuple):
        self.marking_period1, self.marking_period2 = marking_periods

    def _add_exam_score(self, exam:tuple, exam_type:str):
        exam_name, score = exam
        if exam_name not in [subject.name for subject in self.marking_period2.subjects]:
            raise TypeError(f"{exam} {exam_type} exam does not pretain to any of your classes in the last marking period of this semster.")
        if not isinstance(score, int): raise ValueError('Score has to be an Integer!')
        for subject in self.marking_period2.subjects:
            if exam_name == subject.name:
                subject.exams[exam_type] = score



    @classmethod
    def semester1(cls, marking_periods:tuple, midterm_exams:dict):
        semester = cls(marking_periods=marking_periods)
        for exam_name, score in midterm_exams.items():
            semester._add_exam_score(exam=(exam_name, score), exam_type='midterm')
        return semester

    @classmethod
    def semester2(cls, marking_periods:tuple, final_exams:dict):
        semester = cls(marking_periods=marking_periods)
        for exam_name, score in final_exams.items():
            semester._add_exam_score(exam=(exam_name, score), exam_type='final')
        return semester