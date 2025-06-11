import csv

dati = []

with open("kurss.csv", "r", newline = "") as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        dati.append(i)

#------------------------------------------------------------------------------------

studenti_3_kurss = []

for students in dati:
    if int(students["Kurss"]) == 3:
        studenti_3_kurss.append(students)
    
#print(studenti_3_kurss)

#------------------------------------------------------------------------------------

studenti_3_kurss_izcilnieki = []

for izcelnieki in dati:
    if int(izcelnieki["Kurss"]) == 3 and float(izcelnieki["Videja_atzime"]) >= 8.0:
        studenti_3_kurss_izcilnieki.append(izcelnieki)

#print(studenti_3_kurss_izcilnieki)

#-------------------------------------------------------------------------------------

sakartoti_pec_uzvardiem = sorted(dati, key= lambda students: students["Uzvards"])
#print(sakartoti_pec_uzvardiem)

#-------------------------------------------------------------------------------------

sakartoti_pec_videja_atzime_dilstosi = sorted(dati, key= lambda students:float(students["Videja_atzime"]), reverse=True)
#print(sakartoti_pec_videja_atzime_dilstosi)

#-------------------------------------------------------------------------------------

for students in dati:
    #print(f"Vārds: {students["Vards"]}")
    pass

#--------------------------------------------------------------------------------------

datu_skaits = len(dati)
#print(datu_skaits)

atzimju_summa = 0


for students in dati:
    atzimju_summa += float(students["Videja_atzime"])
    
#print(atzimju_summa/len(dati)) #videja atzime

#--------------------------------------------------------------------------------------

max_atzime = 0
max_students = {}

for students in dati:
    if float(students["Videja_atzime"]) > max_atzime:
        max_atzime = float(students["Videja_atzime"])
        max_students = students

#print(max_students)

#-------------------------------------------------------------------------------------

with open("kurss_uzvardi_abc.csv", "w", newline="") as csvfile:
    fieldnames = ["Vards", "Uzvards", "Kurss", "Videja_atzime"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

    writer.writeheader()
    writer.writerows(sakartoti_pec_uzvardiem)