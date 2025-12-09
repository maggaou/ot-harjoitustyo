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
Huom. suorita `git checkout 4f2b2f98c64c93ba69896d216a0818d46b9c1c50` ennen ohjelman kokeilua.

## Viikko 4

### Muutokset:
- ohjelman käynnistys moves-näkymään
- muista näkymistä pääsee takaisin moves-näkymään
- uusi näkymä: liikkeiden luonti
- moves-näkymä/jos käyttäjä ei ole kirjautunut sisään
    - näytä "not logged in"
    - näytä "Login/Create account" painike
- logout/uloskirjautuminen moves-näkymässä näyttää uudestaan moves-näkymän
- moves-näkymästä voi käynnistää yksittäisen liikkeen näkymän

### Muuta
- liikkeiden luonnissa ei ole vielä virheentarkistusta
- liikkeen näkymästä palaaminen moves-näkymään saattaa aiheuttaa tkinter-ongelman että ikkunan sisältö ei päivity ennen kuin käyttäjä vie hiiren ikkunan sisälle
- liikkeen luomisen lomakkeessa ei ole monivalintaelementtejä

## Viikko 5

### Muutokset:
- renderöi liikkeen kentät aina samassa järjestyksessä
- liikkeen poistaminen 
    - näytä poista-nappi liikkeen näkymässä
    - palaa moves-näkymään poistamisen jälkeen
    - näytä poista nappi ainoastaan silloin jos käyttäjä on kirjautunut sisään
- liikkeen muokkaaminen
    - näytä muokkaus-nappi liikkeen näkymässä
    - esitäytä kentät liikkeen muokkauksessa
    - palaa liikkeen näkymään muokkauksen jälkeen
    - näytä liikkeen näkymässä aina uusimmat liikkeen tiedot
- muokkaushistoria
    - näytä muokkaushistoria samassa näkymässä liikkeen muiden tietojen kanssa
    - näytä muokkaushistoriassa
        - muokkauksen päivämäärä ja aika nordic-muodossa
        - kuka muokkauksen teki (käyttäjänimi)
        - alleviivaa muokkaus jos kyseessä on kirjautuneen käyttäjän oma muokkaus
        - älä alleviivaa muokkauksia muissa tapauksissa (esim. jos ei kirjautunut)
    - näytä muokkaushistoria siten että jokainen muokkaus on eri rivillä
    - muokkaushistoria säilyy aina aikajärjestyksessä (listojen tallennus/caput-paketti)

### Muuta
- liikkeiden luonnissa ei ole vielä virheentarkistusta
- liikeiden muokkauksessa ei ole vielä virheentarkistusta
- tyhjä/olematon muokkaus aiheuttaa merkinnän muokkaushistoriaan
- liikkeen näkymästä palaaminen moves-näkymään saattaa aiheuttaa tkinter-ongelman että ikkunan sisältö ei päivity ennen kuin käyttäjä vie hiiren ikkunan sisälle
- sama ongelma on myös liikkeen muokkauksessa
- liikkeen luomisen lomakkeessa ei ole monivalintaelementtejä
- moves-näkymä ei käytä liikkeiden listauksessa mitään ennaltamääriteltyä järjestystä

## Viikko 6

### Muutokset:
- näytä käyttäjälle virheet liikkeen luonnissa ja muokkauksessa:
    - luonti: liikkeellä pitää olla vähintään nimi ja sen täytyy olla vähintään 5 merkkiä
    - muokkaus: älä salli muokkausta joka ei muokkaa mitään
    - muokkaus: älä salli muokkausta jos nimeä ei ole tai jos se on liian lyhyt
- poista ylimääräiset välilyönnit lomaketiedoista liikkeen luonnissa/muokkauksessa
    - näin ollen välilyönnin lisääminen ei ole sallittu muokkaus
- liikkeiden järjestäminen päänäkymässä
    - järjestä lisäyksen, muokkauksen tai nimen perusteella
    - oletus on lisäyksen perusteella
    - jos liikettä ei ole muokattu niin järjestä lisäyksen perusteella
- näytä päänäkymän listassa added/modified/name sarakkeet
- tallenna lisäyksestä myös tarkka kellonaika
- näytä "No moves created yet" jos liikkeitä ei ole luotu
- kuvan näyttäminen liikkeen näkymässä:
    - näytä kuva picture link kentän perusteella (http tai https linkki)
    - kuvan leveys on aina 300px
    - kuvan korkeus skaalautuu kuvasuhteen mukaan
    - näytä "No image to display" jos picture link kenttä on tyhjä
    - näytä "Invalid URL: no scheme supplied" jos linkistä puuttuu http jne
    - näytä "Invalid URL: no host supplied" jos linkki on pelkkä http:// jne
    - näytä "Invalid URL: connection error" jos linkki on muuten virheellinen
    - näytä "Invalid URL: not an image file" jos linkki on toimiva mutta ei sisällä kuvaa
    - näytä "Image read timed out" jos http-kyselyyn ei tule vastausta aikarajan sisällä (0.5 sekuntia)
- jos picture link kenttä on yli 350 merkkiä, niin näytä se useammalla rivillä
- MovesView/järjestäminen: älä lataa liikkeitä uudestaan levyltä
- EditMoveView: back button palaa takaisin Move-näkymään

Testi linkkejä:

https://github.com
(not an image file)

https://www.bjjee.com/wp-content/uploads/2022/02/Head-Arm-Throw.jpg
(ok linkki)

https://i.ytimg.com/vi/lBRACHYmQ48/maxresdefault.jpg
(ok linkki)

https://
(no host supplied)

https://a
(connection error)

## Lopullinen palautus

### Muutokset:

#### Käyttäjän luominen:
- näytä ohjeistus käyttäjänimen ja salasanan luonnille

- Ohjeistus:
    ```
    Username requirements:
    - at lest 4 characters long
    - only lowercase letters
    - no spaces

    Password requirements:
    - must be at least 8 characters
    - only ASCII characters
    ```

- näytä virhe "Username: spaces are not allowed" jos käyttäjänimi sisältää välilyöntejä
- näytä virhe "Username is too short" jos käyttäjänimi on liian lyhyt
- näytä virhe "Password is too short" jos salasana on liian lyhyt
- näytä virhe "Username: only small letters are allowed"
- näytä virhe "Password has non-ASCII characters"
- piilota salasana oletuksena ja näytä se merkeillä ∗
- näytä painike "show password" joka näyttää salasanan
- vaihda painikkeen teksti "show password" <--> "hide password" välillä
- sama painike on myös login-näkymässä