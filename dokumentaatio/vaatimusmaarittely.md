# Vaatimusmäärittely

Ohjelman tarkoitus on tallentaa painiliikkeitä joita valmentajat voivat jakaa keskenään. Liikkeiden talennus tapahtuu tekstitiedostojen avulla jotka sisältävät YAML-metatieto osion.

## Käyttäjät
Sovelluksessa valmentajat ovat eri käyttäjiä.


## Ennen kirjautumista:

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen ✅
    - Käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 3 merkkiä ✅
    - Käyttäjätunnus ei saa sisältää välilyöntejä ✅
    - Käyttäjätunnus saa sisältää vain pieniä kirjaimia ✅
    - Salasanan täytyy olla vähintään 8 merkkiä ✅
    - Salasana ei saa sisältää ei-ASCII merkkejä ✅
    - Käyttäjän luonnissa salasana on piilotettu merkeillä ∗ ✅
    - Salasanan piilotuksen voi kytkeä päälle/pois ✅
- Käyttäjä voi kirjautua järjestelmään ✅
    - Kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus ja salasana kirjautumislomakkeelle ✅
    - Jos käyttäjää ei olemassa, tai salasana ei täsmää, ilmoittaa järjestelmä tästä ✅
    - Kirjautumisessa salasana on piilotettu merkeillä ∗ ✅
    - Salasanan piilotuksen voi kytkeä päälle/pois ✅
- Käyttäjä näkee kaikki painiliikkeet listana mutta ei voi luoda uusia ✅
- Käyttäjä pystyy tarkastelemaan yksittäisen liikkeen tietoja (katso liikkeen näkymä) ✅

### Listaus näkymä:
- näytä "no moves created yet" jos yhtään liikettä ei ole luotu ✅
- näytä "not logged in" ja "login/create account" painikkeet jos ei kirjautunut ✅
- näytä kolme tietosaraketta: added, modified, name ✅
- näytä tietosarakkeet silloin kun liikkeitä on luotu ✅
- järjestä liikkeitä sarakkeiden perusteella ✅
- järjestä oletuksena liikkeet added-sarakkeen perusteella ✅
- jos liikettä ei ole muokattu niin näytä modified sarakkeessa "-" ✅
- järjestäminen muokkauksen perusteella: jos liikettä ei ole muokattu, niin järjestä silloin lisäyksen perusteella (muussa tapauksessa normaalisti muokauksen perusteella) ✅
- näytä liikkeiden nimet alleviivattuna ✅
- hiiren vieminen liikkeen nimen päälle: muuta kursori + ✅
- hiiren vasen klikkaus liikkeen nimen päältä avaa kyseisen liikkeen näkymän ✅

### Liikkeen näkymä
- näytä liikkeiden lisäämisen tiedot (katso liikkeen lisääminen) ✅
- näytä kentät aina samassa järjestyksessä ✅
- näytä liikkeen muokkaushistoria ✅
    - milloin muokattu ✅
    - kuka on tehnyt muokkauksen ✅
- näytä kuka on lisännyt liikkeen alunperin ✅
- näytä lisäämisen ajankohta ✅
- näytä liikkeen yksilöllinen tunniste (uid) ✅
- näytä back-nappi joka palaa takaisin listaus näkymään ✅
- näytä liikkeen kuva ✅
- jos kuvan linkkiä ei ole niin näytä "no image to display" ✅
- näytä relavantit virheet jos kuvan linkki on virheellinen ✅
    - Invalid URL: no scheme supplied ✅
    - Invalid URL: no host supplied ✅
    - Invalid URL: connection error ✅
    - Invalid URL: not an image file ✅
    - Image read timed out. (read timeout=0.5) ✅
- näytettävän kuvan leveys on aina 300px ✅
- näytettävän kuvan korkeus skaalautuu kuvasuhteen mukaan ✅


## Kirjautumisen jälkeen:
- näytä listausnäkymässä logged in `käyttäjän nimi` ✅
- Käyttäjä voi luoda uuden painiliikkeen ✅
    - näytä listausnäkymässä painike create new painike ✅
- Käyttäjä voi kirjautua ulos järjestelmästä ✅
    - näytä listausnäkymässä logout painike ✅
    - uloskirjautuminen näyttää listaus-näkymän ✅

### Liikkeen lisääminen

Liikkeen lisääminen sisältää seuraavat kentät:
- nimi ✅
- sisältö ✅
- kuva (ulkoinen linkki kuvaan) ✅
- painimuoto ✅
- ikäryhmä ✅
- vaikeusaste ✅
- linkki (ulkoinen referenssi) ✅
- lisäksi tallennus käyttää implisiittisiä metatietoja:
    - kuka on tehnyt tämän tallennuksen alunperin ✅
    - milloin tallennus on tehty ✅

#### Muuta
- tallenna lisäyspäivämääärä muodossa DD.MM.YYYY HH:ss ✅
- liikkeen luominen tyhjällä nimellä ei ole sallittua ✅
- liikkeen nimen täytyy olla vähintään 5 merkkiä ✅
- näytä liikkeen lisäämisen kentät aina samassa järjestyksessä ✅
- poista ylimääräiset välilyönnit lomaketietojen lopusta/alusta ✅

### Liikkeen näkymä (kirjautuneena)

- alleviivaa muokkaushistoriassa omat muokkaukset ✅
- näytä delete ja edit napit ✅

### Liikkeen muokkaus ja poisto
- liikkeen muokkaus ja poisto tapahtuu liikkeen näkymän kautta (joka on kuvattu yllä) ✅
- poistaminen ohjaa moves-näkymään ✅
- liikkeen muokkaus ei ole mahdollista jos mitään muutoksia ei ole tehty ✅
- liikkeen muokkauksen vaatimukset ovat samat liikkeen luomisen kanssa ✅
- liikkeen muokkauksen voi peruuttaa back-napilla ✅
- liikkeen muokkauksen back-nappi vie takaisin kyseisen liikkeen näkymään ✅
- onnistunut liikkeen muokkaus näyttää kyseisen liikkeen muokatuilla tiedoilla ✅
- tallenna liikkeen muokkausajankohta muodossa DD.MM.YYYY HH:ss ✅
- tallenna liikkeen muokkauksen tekijä ✅
- poista ylimääräiset välilyönnit lomaketietojen lopusta/alusta ✅
