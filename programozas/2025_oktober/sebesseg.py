SEBKORLATOZAS = 2
VAROS = 4
VÁROS_VÉGE = "]"
f = open("ut.txt")
összeméter = f.readline()
print("Összes méter:", összeméter)
út = []
for sor in f:
    rekord = sor.split()
    rekord2 = {
        "km": rekord[0], "jel":rekord[1]
    }
    út.append(rekord2)
i=0
for sor in út:
    print(i, " --> ", sor["km"], " , ", sor["jel"], " - ", len(sor["jel"]))
    i += 1
print("\n2. feladat")
print("A települések neve:")
for sor in út:
    if len(sor["jel"]) > VAROS:
        print(sor["jel"])
print("\n3. feladat")
print("A települések neve:")
#szakasz_str = input("Adja meg a vizsgált szakasz hosszát km-ben! ")
szakasz_str = "71"
szakasz = float(szakasz_str) * 1000
legkisebb = 9999
for sor in út:
    if float(sor["km"]) > szakasz:
        break
    if len(sor["jel"]) == SEBKORLATOZAS:
        legkisebb = min(int(sor["jel"]),legkisebb)
print(f"Az első {szakasz_str} km-en {legkisebb} km/h volt a legalacsonyabb megengedett sebesség.")
print("\n4. feladat")
összes_város = 0
for sor in út:
    if len(sor["jel"]) > VAROS:
        város_eleje = float(sor["km"])
    if sor["jel"] == VÁROS_VÉGE:
        összes_város += float(sor["km"]) - város_eleje
százalék = összes_város / float(összeméter) * 100
print(f"Az út {százalék:.2f} százaléka vezet településen belül.")
print("\n5. feladat")
# város = input("Adja meg egy település nevét! ")
város = "Varos010"
város_eleje = -1
táblák = 0
városi_km = 0
for sor in út:
    if sor["jel"] == város:
        város_eleje = int(sor["km"])
    if város_eleje > 0:
        if len(sor["jel"]) == SEBKORLATOZAS:
            táblák += 1
        if sor["jel"] == VÁROS_VÉGE:
            városi_km = int(sor["km"]) - város_eleje
            break
print(f"A sebességkorlátozó táblák száma: {táblák}")
print(f"Az út hossza a településen belül {városi_km} méter.")
print("\n6. feladat")
város = input("Adja meg egy település nevét! ")
keresett = False
elso_nev = ""
elso_tav = 0
hatso_nev = ""
hatso_tav = 0
keresett_eleje = 0
keresett_vege = 0
for sor in út:
    
    if len(sor["jel"]) > VAROS:
        varos_nev_temp = sor["jel"]
        varos_tav_eleje = int(sor["km"])
        if sor["jel"] == város:
            keresett = True
            keresett_eleje = int(sor["km"])
        if keresett_vege != 0:
            hatso_nev = sor["jel"]
            hatso_tav = int(sor["km"])

        
    if sor["jel"] == VÁROS_VÉGE:
        varos_tav_vege = int(sor["km"])
        if keresett and keresett_vege == 0:
            keresett_vege = int(sor["km"])
        if keresett_vege == 0:
            elso_nev = varos_nev_temp
            elso_tav = varos_tav_vege
if keresett_eleje - elso_tav < hatso_tav - keresett_vege:
    print(f"A legközelebbi település:{elso_nev}" )
else:
    print(f"A legközelebbi település:{hatso_nev}" )


