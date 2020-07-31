from school.student import Student
from school.subject import Subject


paul = Student(name='Paul')
paul.year = 11
paul.mp = 1


CAD1 = Subject.half_year(name='CAD 1: Introduction to CADD')
Graphics1 = Subject.half_year(name='Graphics 1')
H_Algebra2 = Subject.honors(name='H Algebra 2')
H_Ancient_World_History = Subject.honors(name='H Ancient World History')
H_English9 = Subject.honors(name='H English 9')
H_Physical_Science = Subject.honors(name='H Physical Science 1')
Spanish2 = Subject.language(name='Spanish 2')
gym = Subject.half_year(name='Sports & Fitness Course 1-Boys')

subjects9 = [
    CAD1,
    Graphics1,
    H_Algebra2,
    H_Ancient_World_History,
    H_English9,
    H_Physical_Science,
    Spanish2,
    gym
]

CAD1.mp[1].grade = 99.00
CAD1.mp[2].grade = 99.00

Graphics1.mp[3].grade = 98.00
Graphics1.mp[4].grade = 99.00

H_Algebra2.mp[1].grade = 94.00
H_Algebra2.mp[2].grade = 97.00
H_Algebra2.sem1.exam = 100
H_Algebra2.mp[3].grade = 95.00
H_Algebra2.mp[4].grade = 98.00
H_Algebra2.sem2.exam = 100

H_Ancient_World_History.mp[1].grade = 95.00
H_Ancient_World_History.mp[2].grade = 92.00
H_Ancient_World_History.sem1.exam = 92
H_Ancient_World_History.mp[3].grade = 93.00
H_Ancient_World_History.mp[4].grade = 95.00
H_Ancient_World_History.sem2.exam = 94

H_English9.mp[1].grade = 84.00
H_English9.mp[2].grade = 83.00
H_English9.sem1.exam = 90
H_English9.mp[3].grade = 95.00
H_English9.mp[4].grade = 93.00
H_English9.sem2.exam = 87

H_Physical_Science.mp[1].grade = 91.00
H_Physical_Science.mp[2].grade = 94.00
H_Physical_Science.sem1.exam = 95
H_Physical_Science.mp[3].grade = 95.00
H_Physical_Science.mp[4].grade = 92.00
H_Physical_Science.sem2.exam = 99

Spanish2.mp[1].grade = 93.00
Spanish2.mp[2].grade = 94.00
Spanish2.mp[3].grade = 93.00
Spanish2.mp[4].grade = 95.00

gym.mp[3].grade = 99.00
gym.mp[4].grade = 94.00





AP_World_History = Subject.advanced_placement(name='AP World History')
CADD2 = Subject.half_year(name='CADD 2')
H_Biology = Subject.honors(name='H Biology')
H_Computer_Programming = Subject.half_year_honors(name='H Computer Programming')
H_Enlgish10 = Subject.honors(name='H English 10')
H_Geometry = Subject.honors(name='H Geometry')
Python = Subject.half_year(name='Intro to Python')
Spanish3 = Subject.language(name='Spanish 3')
TAG = Subject.half_year(name='Team Aerobic Games')

subjects10 = [
    AP_World_History,
    CADD2,
    H_Biology,
    H_Computer_Programming,
    H_Enlgish10,
    H_Geometry,
    Python,
    Spanish3,
    TAG
]

AP_World_History.mp[1].grade = 89.00
AP_World_History.mp[2].grade = 90.00
AP_World_History.sem1.exam = 68
AP_World_History.mp[3].grade = 87.00
AP_World_History.mp[4].grade = 100.00

CADD2.mp[3].grade = 88.00
CADD2.mp[4].grade = 96.00

H_Biology.mp[1].grade = 94.00
H_Biology.mp[2].grade = 91.00
H_Biology.sem1.exam = 94
H_Biology.mp[3].grade = 95.00
H_Biology.mp[4].grade = 91.00

H_Computer_Programming.mp[3].grade = 97.00
H_Computer_Programming.mp[4].grade = 100.00

H_Enlgish10.mp[1].grade = 85.00
H_Enlgish10.mp[2].grade = 96.00
H_Enlgish10.sem1.exam = 77
H_Enlgish10.mp[3].grade = 93.00
H_Enlgish10.mp[4].grade = 91.00

H_Geometry.mp[1].grade = 95.00
H_Geometry.mp[2].grade = 96.00
H_Geometry.sem1.exam = 100
H_Geometry.mp[3].grade = 98.00
H_Geometry.mp[4].grade = 96.00

Python.mp[1].grade = 100.00
Python.mp[2].grade = 97.00

Spanish3.mp[1].grade = 91.00
Spanish3.mp[2].grade = 91.00
Spanish3.mp[3].grade = 93.00
Spanish3.mp[4].grade = 89.00

TAG.mp[1].grade = 93.00
TAG.mp[2].grade = 96.00





paul.high_school[9].extend_subjects(subjects=subjects9)
paul.high_school[10].extend_subjects(subjects=subjects10)

# TODO credits don't show with 3 decimal points
# paul.write_report_card(year=9, mp=4)
# paul.write_report_card(year=10, mp=4)

# TODO test
# NOTE run all tests before this one
paul.write_transcript(year=10)