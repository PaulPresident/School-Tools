# Import Depedencies


# Import Files
import Storage
import EnterGrades
import DisplayGrades
import UpdateGrades
import UnWeightedNGA
import WeightedNGA


request = 0

while request != 'quit':

    request = input('''
NGA Calculator

Value\tCommand

  1  \tEnter Grades
  2  \tDisplay Grades
  3  \tUpdate Grades
  4  \tUnWeighted NGA
  5  \tWeighted NGA

**quit to exit**

''')

    if request == '1':
        EnterGrades.Enter_Grades()
    elif request == '2':
        DisplayGrades.Display_Grades()
    elif request == '3':
        UpdateGrades.Update_Grades()
    elif request == '4':
        UnWeightedNGA.UnWeighted_NGA()
    elif request == '5':
        WeightedNGA.Weighted_NGA()