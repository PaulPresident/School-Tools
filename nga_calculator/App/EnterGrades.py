# Import Storage
import Storage

# Appends Grades to their respective Lists
def Enter_Grades():
    MP = int(input('\nEnter MP\n'))
    
    Storage.AP_Modern_World_History.insert(MP, int(input('\nEnter AP Modern World History Grade\n')))
    Storage.H_English_10.insert(MP, int(input('\nEnter H English 10 Grade\n')))
    Storage.H_Geometry.insert(MP, int(input('\nEnter H Geometry Grade\n')))
    Storage.H_Biology.insert(MP, int(input('\nEnter H Biology Grade\n')))
    Storage.Spanish_3.insert(MP, int(input('\nEnter Spanish 3 Grade\n')))
    Storage.Elective_1.insert(MP, int(input('\nEnter Elective 1 Grade\n')))
    Storage.Elective_2.insert(MP, int(input('\nEnter Elective 2 Grade\n')))