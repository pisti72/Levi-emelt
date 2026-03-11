-- 1. feladat
SELECT diakok.nev FROM diakok WHERE diakok.telepules = "Barnamalom";
-- 2. feladat
SELECT orak.datum, orak.terem, orak.orasorszam FROM orak where orak.targy = "angol" ORDER BY orak.datum, orak.orasorszam;
-- 3. feladat
SELECT orak.csoport, orak.targy, orak.datum from orak where (orak.targy = "matematika" or orak.targy = "fizika") and orak.csoport like "9%";
-- 4. feladat
SELECT diakok.telepules, count(diakok.nev) as darab from diakok GROUP BY diakok.telepules order BY darab DESC ;
-- 5. feladat a:
SELECT DISTINCT(orak.targy) from orak order by orak.targy;
-- 5. feladat b:
SELECT orak.targy from orak group by orak.targy;
-- 6. feladat
SELECT diakok.nev, diakok.email, diakok.telefon from diakok, kapcsolo, orak where kapcsolo.diakid = diakok.id and kapcsolo.oraid = orak.id and orak.tanar = "Angol Anna" and orak.datum = "2028.11.10.";
-- 7. feladat
SELECT diakok.nev from diakok where diakok.telepules = (SELECT diakok.telepules from diakok where diakok.nev ="Majer Melinda") and diakok.nev != "Majer Melinda";
-- 8. feladat
-- SELECT orak.datum, orak.orasorszam, orak.targy, orak.tanar, orak.ferohely as szabad from orak where
SELECT kapcsolo.oraid, orak.ferohely, count(kapcsolo.diakid)
from kapcsolo, orak
WHERE kapcsolo.oraid = orak.id
GROUP BY kapcsolo.orai
