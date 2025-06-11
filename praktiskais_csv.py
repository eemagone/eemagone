import csv

dati = []

with open("busstops.csv", "r",  newline = "", encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        dati.append(i)

#print(dati)

Ogre = []

for i in dati:
    if (i["County"]) == "Ogres novads":
        Ogre.append(i)

#print(Ogre)
sakartot_ogri = []

sakartot_ogri = sorted(Ogre, key= lambda i: i["Stop_name"])

summa_l = 0
summa_k = 0

for i in sakartot_ogri : 
    if i["Street"] == "":
        i["Street"] = "Nav"
        #print(f"{i["Street"]} - {i["Stop_name"]}...")
        pass
    else:
        #print(f"{i["Street"]} - {i["Stop_name"]}...")
        pass

for i in sakartot_ogri :
    if i["Road_side"] == "Labā":
        summa_l += 1
        
    else:
        summa_k += 1
        
print(f"Ogres novadā pieturas ceļa labajā pusē: {summa_l}")
print(f"Ogres novadā pieturas ceļa kreisajā pusē: {summa_k}")