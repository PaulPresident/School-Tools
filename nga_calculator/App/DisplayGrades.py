# Import Storage
import Storage

# Display Grades
def Display_Grades():
    MP = int(input('\nEnter MP\n'))

    print(f'''\n\n
MP {MP} Grades:

Grade\tClass
{Storage.AP_Modern_World_History[MP]}%\tAP Modern World History
{Storage.H_English_10[MP]}%\tH English 10
{Storage.H_Geometry[MP]}%\tH Geometry
{Storage.H_Biology[MP]}%\tH Biology
{Storage.Spanish_3[MP]}%\tSpanish 3
{Storage.Elective_1[MP]}%\tElective 1
{Storage.Elective_2[MP]}%\tElective 2
''')