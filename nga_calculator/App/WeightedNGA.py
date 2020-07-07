# Import Storage
import Storage

# Calculate Weighted NGA
def Weighted_NGA():
    MP = int(input('\nEnter MP\n'))

    Weighted_HIST_Grade = float(Storage.AP_Modern_World_History[MP]) * 1.10
    Weighted_ENG_Grade = float(Storage.H_English_10[MP]) * 1.05
    Weighted_GEO_Grade = float(Storage.H_Geometry[MP]) * 1.05
    Weighted_BIO_Grade = float(Storage.H_Biology[MP]) * 1.05
    Weighted_SPAN_Grade = float(Storage.Spanish_3[MP]) * 1.00
    Weighted_Elective_1_Grade = float(Storage.Elective_1[MP]) * 0.50
    Weighted_Elective_2_Grade = float(Storage.Elective_2[MP]) * 0.50

    Storage.Weighted_NGA.append((Weighted_HIST_Grade + Weighted_ENG_Grade + Weighted_GEO_Grade + Weighted_BIO_Grade + Weighted_SPAN_Grade + Weighted_Elective_1_Grade + Weighted_Elective_2_Grade) / 6)

    print(f'''
MP \tWeighted NGA
{MP}\t{round(Storage.Weighted_NGA[MP], 3)}
''')