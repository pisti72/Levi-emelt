kartyak = []
with open("bedat.txt") as adatok:
    for lines in adatok:
        sor = lines.strip().split()
        kartyak.append(sor)
print("2. feladat")
print(f"Az első tanuló {kartyak[0][1]}-kor lépett be a főkapun.")
print(f"Az utolsó tanuló {kartyak[-1][1]}-kor lépett ki a főkapun.")

print("3. feladat")

with open("kesok.txt", "wt", encoding="utf-8") as f:
    for sor in kartyak:
        if(sor[1] > "07:50" and sor[1] < "08:15"):
            print(sor[1], sor[0], file=f)

print("4. feladat")
cnt = 0
for sor in kartyak:
    if(sor[2] == "3"):
        cnt += 1
print(f"A menzán aznap {cnt} tanuló ebédelt.")

print("5. feladat")
kolcson = []
for sor in kartyak:
    if(sor[2] == "4" and sor[0] not in kolcson):
        kolcson.append(sor[0])
print(f"Aznap {len(kolcson)} tanuló kölcsönzött a könyvtárban.")
if(cnt < len(kolcson)):
    print("Többen voltak, mint a menzán.")
else:
    print("Nem voltak többen, mint a menzán.")

print("6. feladat")
erkez = []
for sor in kartyak:
    if(sor[1] <= "10:45" and sor[2] == "1"):
        erkez.append(sor[0])
kilep = []
for sor in kartyak:
    if(sor[2] == "2" and sor[1] < "10:45"):
        kilep.append(sor[0])
for sor in kartyak:
    if(sor[1] >= "10:50" and sor[1] <= "11:00" and sor[0] in erkez and sor[0] not in kilep and sor[2] == "1"):
        print(f"{sor[0]}", end=" ")
        
print()
print("7. feladat")
#tanulo = input("Egy tanuló azonosítója:")
tanulo = "ZOOM"
erkez = ""
tavoz = ""
for sor in kartyak:
    if(sor[0] == tanulo and erkez == ""):
        erkez = sor[1]
    elif(sor[0] == tanulo):
        tavoz = sor[1]
ido = erkez.split(":")
erkez_ido = (int(ido[0]) * 60) + int(ido[1])
ido = tavoz.split(":")
tavoz_ido = (int(ido[0]) * 60) + int(ido[1])
ossz = tavoz_ido - erkez_ido
print(f"A tanuló érkezése és távozása között {ossz//60} óra {ossz%60} perc telt el.")






