# ALD-Semestralka
Složka api obsahuje jednoduché REST api napsané v Ruby, které příjimá GET request, který vygeneruje mapu dlaždic ve formátu JSON. Dostupné typy dlaždic je možné přidávat v classe Map, kde jejich formát je pole o 5 prvcích. První 4 prvky určují zda na stranách cesta pokračuje nebo ne, poslední prvek uchovává název dlaždice.
Složka client obsahuje jednoduchý grafický client napsaný v Pythonu, který provádí request na REST api a poté namapuje obrázky ze složky "tilesets" dle JSONu, který dostal jako odpověď.
