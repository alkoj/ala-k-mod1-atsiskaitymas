Duomenų Parsinimo Projektas

Šis projektas apima du skriptus duomenų parsinimui iš svetainių: vieną iš [https://www.gintarine.lt](https://www.gintarine.lt/maistas-ir-papildai-sportininkams) 
ir kitą iš [https://www.lrytas.lt](https://www.lrytas.lt/it) .
Kiekvienas skriptas išgauna skirtingus duomenis ir išsaugo juos CSV formatu.

Turinys

- Įdiegimas
- Naudojimas
- Testavimas
- Priklausomybės


Įdiegimas

Klonuokime repo:

git clone https://github.com/alkoj/ala-k-mod1-atsiskaitymas.git


Naudojimas:

  Parsinimas iš Gintarine

Norėdami atlikti duomenų parsinimą iš Gintarine, vykdykime šį kodą: 

from ala_module.scraper_gintarine import scrape_products 

scrape_products(time_limit=20) 

Duomenys yra išsaugoti faile products.csv.

  Parsinimas iš Lrytas

Norėdami atlikti duomenų parsinimą iš Lrytas, vykdykime šį kodą: 

from ala_module.scraper_lrytas import scrape_lrytas 

scrape_lrytas()  

Duomenys yra išsaugoti faile sorted_data.csv.


Priklausomybės

Projekte naudojamos šios bibliotekos:

requests — HTTP užklausoms

beautifulsoup4 — HTML parsinimui

lxml — HTML analizavimui naudojant XPath

csv — darbui su CSV failais
