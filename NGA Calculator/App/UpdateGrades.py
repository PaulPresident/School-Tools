# Import Storage
import Storage

# Update Grades (Useful if Can Save)
def Update_Grades():
    MP = int(input('\nEnter MP\n'))
    change = 0

    while change != 'done':
        change = input('''
NGA Calculator

Value\tCommand

  1  \tAP Modern World History
  2  \tH English 10
  3  \tH Geometry
  4  \tH Biology
  5  \tSpanish 3
  6  \tElective 1
  7  \tElective 2

**done to exit**

''')

        if change == '1':
            del Storage.AP_Modern_World_History[MP]
            Storage.AP_Modern_World_History.insert(MP, int(input('\nEnter AP Modern World History Grade\n')))
        elif change == '2':
            del Storage.H_English_10[MP]
            Storage.H_English_10.insert(MP, int(input('\nEnter H English 10 Grade\n')))
        elif change == '3':
            del Storage.H_Geometry[MP]
            Storage.H_Geometry.insert(MP, int(input('\nEnter H Geometry Grade\n')))
        elif change == '4':
            del Storage.H_Biology[MP]
            Storage.H_Biology.insert(MP, int(input('\nEnter H Biology Grade\n')))
        elif change == '5':
            del Storage.Spanish_3[MP]
            Storage.Spanish_3.insert(MP, int(input('\nEnter Spanish 3 Grade\n')))
        elif change == '6':
            del Storage.Elective_1[MP]
            Storage.Elective_1.insert(MP, int(input('\nEnter Elective 1 Grade\n')))
        elif change == '6':
            del Storage.Elective_2[MP]
            Storage.Elective_2.insert(MP, int(input('\nEnter Elective 2 Grade\n')))

