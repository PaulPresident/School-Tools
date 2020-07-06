# Import Storage
import Storage

# Calculate UnWeighted NGA
def UnWeighted_NGA():
    MP = int(input('\nEnter MP\n'))

    Storage.UnWeighted_NGA.append(int((Storage.AP_Modern_World_History[MP] + Storage.H_English_10[MP] + Storage.H_Geometry[MP] + Storage.H_Biology[MP] + Storage.Spanish_3[MP] + Storage.Elective_1[MP] + Storage.Elective_2[MP])/7))

    print(f'''
MP \tUnWeighted NGA
{MP}\t{round(Storage.UnWeighted_NGA[MP], 3)}
''')