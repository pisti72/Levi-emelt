SELECT hirfolyam.megnevezes, felhasznalo.veznev, felhasznalo.utonev, felhasznalo.email FROM `hirfolyam` INNER JOIN felhasznalo ON hirfolyam.moderator=felhasznalo.id;
---
SELECT uzenet.tartalom FROM uzenet WHERE uzenet.tartalom LIKE '%bike%' OR uzenet.tartalom LIKE '%bicikli%';
---
SELECT felhasznalo.veznev, felhasznalo.utonev
FROM felhasznalo
GROUP BY felhasznalo.veznev, felhasznalo.utonev
HAVING COUNT(*) > 1;
---
SELECT hirfolyam.megnevezes, COUNT(*) AS darab
FROM hirfolyam, uzenet
WHERE hirfolyam.id = uzenet.h_id
GROUP BY hirfolyam.id
ORDER BY darab DESC