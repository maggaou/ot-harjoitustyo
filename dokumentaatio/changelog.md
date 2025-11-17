> [!Note]
> Changelogin ylläpitäminen on yleinen tapa dokumentoida merkittävät muutokset, joita ohjelmistoprojektissa tapahtuu sen kehityksen edetessä. Lisää projektin dokumentaatio-hakemistoon tiedosto changelog.md ja dokumentoi siihen jokaisen viikon aikana tapahtuneet merkittävät muutokset. Merkittäviä muutoksia ovat esimerkiksi uudet käyttäjälle näkyvät toiminnallisuudet, suuremmat arkkitehtuuriset muutokset (esimerkiksi uudet luokat ja niiden vastuualueet) ja uudet testauksen kohteet.

## Viikko 3

### Muutokset:
- tietokantayhteys (sqlite3) UserRepository ja testit tähän liittyen
- tiedostoyhteys MovesRepository, caput paketti ja testit
- ohjelman toimintalogiikka MovesService ja testit
- käyttöliittymä (tkinter) ja tämän nopea manuaalinen testaus

### Muuta
Puuttuu vielä varsinaiset toiminnot kuten uuden liikkeen luominen. Linux sopivuutta ei ole vielä kokeiltu.

Liikkeitä voi luoda manuaalisesti `data/my-moves/` kansioon, esim.

*111.md*:
```txt
---
name: my nice move 1
style:
age_group:
difficulty:
original_creator:
date_submitted:
picture_link:
reference:
id: 111
---
jeihou
```

*222.md*:
```txt
---
name: my nice move 2
style:
age_group:
difficulty:
original_creator:
date_submitted:
picture_link:
reference:
id: 222
---
jeihou
```
## Viikko 4

### Muutokset
- korjattu pylintin ehdottamat virheet
  - move.py: korjaamatta _too-many-instance-attributes_
