# Multiparadigmás programozási nyelvek beadandó feladat
## Krigovszki Bálint KDPEQ8 - 2022

#

## Dolgozó management system

Az alkalmazás egy adatbázishoz kapcsolódik, melyből táblázatba kilistázza a benne található dolgozókat és adataikat.

A dolgozókra az alap CRUD műveletek vannak implementálva. Dupla kattintással ki tudunk jelölni egy dolgozót a táblázatból a további műveletekhez. Ezután a dolgozókkal végezhető műveletek:

- Új dolgozó felvétele az adatbázisba
    - az ID mezőbe bármi írható, az adatbázis automatikusan generál azonosítót a dolgozóhoz
- Dolgozó adatainak módosítása
- Dolgozó törlése az adatbázisból

A táblázatban lehetőség van keresésre vezetéknév, keresztnév, életkor és város alapján.

A táblázatban megjelenített adatokat tudjuk exportálni CSV fájlba, valamint CSV fájlból is tudunk betölteni dolgozókat az alkalmazásba. Szűrés után csak a táblázatban jelen lévő adatok kerülnek exportálásra. Adatokat az adatbázisba is tudunk menteni.