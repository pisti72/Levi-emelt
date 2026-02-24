file = open("kiadas.txt")
konyvek = list()
ÉV = 0
NEGYED_ÉV = 1
EREDET = 2
LEÍRÁS = 3
PÉLDÁNYSZÁM = 4

for sor in file:
    konyvek.append(sor.split(";"))

print("2-es feladat")

#nev = input("Szerző neve:")
nev = "Benedek Elek"
db = 0
for k in konyvek:
    if(k[LEÍRÁS].find(nev) != -1):
        db += 1
if(db > 0):
    print(db, "könyvkiadás")
else:
    print("Nem adtak ki")

print("3-as feladat")
nagy = 0
db = 0
for k in konyvek:
    nagy = max(nagy, int(k[PÉLDÁNYSZÁM]))
for k in konyvek:
    if( nagy == int(k[PÉLDÁNYSZÁM])):
        db += 1

print("Legnagyobb pélányszám:", nagy, "előfordult", db, "alkalommal")

print("4-es feladat")

for k in konyvek:
    if(k[EREDET] == "kf" and int(k[PÉLDÁNYSZÁM]) > 40000):
        print(f"{k[ÉV]}/{k[NEGYED_ÉV]}. {k[LEÍRÁS]}")
        break 

print("5-ös feladat")
évek = []

for i in range(0,4):
    sor = list()
    sor.append(2020+i)
    for j in range(0,4):
        sor.append(0)
    évek.append(sor)

ev = 0
for k in konyvek:
    for é in évek:
        if int(k[ÉV]) == é[0]:
            if k[EREDET] == "ma":
                é[1] += 1

for é in évek:
    print(é)

        
        


