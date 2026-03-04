file = open("kiadas.txt")
könyvek = list()
ÉV = 0
NEGYED_ÉV = 1
EREDET = 2
LEÍRÁS = 3
PÉLDÁNYSZÁM = 4

for sor in file:
    könyvek.append(sor.split(";"))

print("2-es feladat")

#nev = input("Szerző neve:")
nev = "Benedek Elek"
db = 0
for k in könyvek:
    if(k[LEÍRÁS].find(nev) != -1):
        db += 1
if(db > 0):
    print(db, "könyvkiadás")
else:
    print("Nem adtak ki")

print("3-as feladat")
nagy = 0
db = 0
for k in könyvek:
    nagy = max(nagy, int(k[PÉLDÁNYSZÁM]))
for k in könyvek:
    if( nagy == int(k[PÉLDÁNYSZÁM])):
        db += 1

print("Legnagyobb pélányszám:", nagy, "előfordult", db, "alkalommal")

print("4-es feladat")

for k in könyvek:
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
for k in könyvek:
    for é in évek:
        if int(k[ÉV]) == é[0]:
            if k[EREDET] == "ma":
                é[1] += 1
                é[2] += int(k[PÉLDÁNYSZÁM])
            if k[EREDET] == "kf":
                é[3] += 1
                é[4] += int(k[PÉLDÁNYSZÁM])
fejléc = ["Év","Magyar kiadás","Magyar példányszám","Külföldi kiadás","Küldföldi példányszám"]
fejléc_txt = ""
for f in fejléc:
    fejléc_txt += f + "\t"
print(fejléc_txt)
for é in évek:
    sor = ""
    for o in é:
        sor += str(o) + "\t\t"
    print(sor)
print("\n5b. feladat")
file = open("tabla.html", "w")
fejléc_html = "<table>\n<tr>"
for f in fejléc:
    fejléc_html += "<th>" + f + "</th>"
fejléc_html += "</tr>\n"
file.write(fejléc_html)

print("6. feladat:")
print("könyvek:")

keresett = ""
keresett_peldanyszam = 0
count = 0
x = []
count2 = 0
for k in könyvek:
    db = 0
    keresett = k[LEÍRÁS]
    keresett_peldanyszam = k[PÉLDÁNYSZÁM]
    for i in range(count, len(könyvek)):
        if(keresett == könyvek[i][LEÍRÁS] and keresett_peldanyszam < könyvek[i][PÉLDÁNYSZÁM]):
            db += 1
    if(db >= 2):
        if(not(keresett in x)):
            x.append(keresett)
            count2 += 1
    count += 1
print(x)



        
        


