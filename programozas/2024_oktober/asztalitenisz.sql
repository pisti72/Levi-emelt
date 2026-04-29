-- 2
SELECT ev, versenyszam.nev
FROM versenyszam, bajnok, jatekos
WHERE versenyszam.id = vsz_id AND jatekos.id = jatekos_id AND jatekos.nev = "Harczi Zsolt"
-- 3
SELECT ev FROM versenyszam, bajnok
WHERE versenyszam.id = bajnok.vsz_id 
AND versenyszam.nev = "vegyes páros"
order by ev ASC
limit 1
-- 4
SELECT COUNT(IF(neme = 1, 1, null )) AS Férfi, COUNT(IF(neme = 0, 1, null)) AS Nők
FROM jatekos
-- 5
SELECT DISTINCT egyesulet.orszag
FROM egyesulet, bajnok
WHERE bajnok.egyesulet_id = egyesulet.id AND bajnok.ev >= 2000 AND egyesulet.orszag != "Magyarország"
-- 6
SELECT jatekos.nev
FROM egyesulet, bajnok, jatekos
WHERE egyesulet.id = bajnok.egyesulet_id AND jatekos.id = bajnok.jatekos_id AND egyesulet.nev = "MTK"
group by jatekos.nev 
ORDER BY jatekos.neme, jatekos.nev
-- 7
SELECT jatekos.nev, bajnok.ev , versenyszam.nev
FROM jatekos, bajnok, versenyszam
WHERE jatekos.id = bajnok.jatekos_id AND versenyszam.id = bajnok.vsz_id
GROUP BY jatekos.nev
HAVING COUNT(bajnok.ev) = 1
ORDER BY jatekos.nev
-- 8
SELECT jatekos.nev, MAX(bajnok.ev) - MIN(bajnok.ev) as evek, MAX(bajnok.ev), MIN(bajnok.ev) 
FROM jatekos, bajnok
WHERE jatekos.id = bajnok.jatekos_id
GROUP BY jatekos.nev
HAVING evek >= 10
ORDER BY jatekos.nev
-- 9 
select DISTINCT jatekos.nev
from jatekos, bajnok, versenyszam
where bajnok.ev in (SELECT bajnok.ev
FROM jatekos, bajnok, versenyszam
WHERE jatekos.id = bajnok.jatekos_id and versenyszam.id = bajnok.vsz_id AND jatekos.nev = "Pergel Szandra" AND versenyszam.nev = "vegyes páros") and jatekos.id = bajnok.jatekos_id AND  bajnok.vsz_id = versenyszam.id and versenyszam.nev = "vegyes páros" and jatekos.nev != "Pergel Szandra"