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
    if len(sor["jel"]) > 4:
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
    if len(sor["jel"]) == 2:
        if int(sor["jel"]) < legkisebb:
            legkisebb = int(sor["jel"])
print(f"Az első {szakasz_str} km-en {legkisebb} km/h volt a legalacsonyabb megengedett sebesség.")