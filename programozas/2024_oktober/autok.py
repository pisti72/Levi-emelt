file = open("jeladas.txt",encoding="UTF-8")
jelek = []

RSZÁM = 0
ÓRA = 1
PERC = 2
KMH = 3

#1. feladat

for sor in file:
    s_list = sor.split()
    jelek.append(s_list)

#2. feladat
utolsó = jelek[-1]
print("2. feladat:")
print(f"Az utolsó jeladás időpontja {utolsó[ÓRA]}:{utolsó[PERC]}, a jármű rendszáma {utolsó[RSZÁM]}" )

#3. feladat
print("3. feladat:")
elso = jelek[0][RSZÁM]
idopontok = ""
for s in jelek:
    if s[RSZÁM] == elso:
        idopontok += s[ÓRA] + ":" + s[PERC] + " "
print(f"Az első jármű: {elso}")
print(f"Jeladásainak időpontjai: {idopontok}")

#4. feladat
print("4. feladat")
ora = "6" #input("Kérem adja meg az órát: ")
perc = "54" #input("Kérem, adja meg a percet: ")
db = 0
for s in jelek:
    if s[ÓRA] == ora and s[PERC] == perc:
        db += 1
print(f"A jeladások száma: {db}")

#5. feladat
print("5. feladat")
max = 0
for s in jelek:
    if max < int(s[KMH]):
        max = int(s[KMH])
print(f"A legnagyobb sebesség km/h: {max}")
jarmuvek = ""
for s in jelek:
    if int(s[KMH]) == max:
        jarmuvek += s[RSZÁM] + " "
print(f"A járművek: {jarmuvek}")

#6. feladat
print("6. feladat")

km = 0
ido = -1
keresett = input("Kérem, adja meg a rendszámot: ")
for s in jelek:
    if s[RSZÁM] == keresett:
        if ido == -1:
            ido = 60 * int(s[ÓRA]) + int(s[PERC])
            print(f"{s[ÓRA]}:{s[PERC]} 0.0 km")
        else:
            uj_ido = 60 * int(s[ÓRA]) + int(s[PERC])
            uj_km = ((uj_ido - ido) / 60) * int(s[KMH])
            km = km + uj_km
            ido = uj_ido
            print(f"{s[ÓRA]}:{s[PERC]} {round(km, 1)} km")
if ido == -1:
    print("Nincs")


