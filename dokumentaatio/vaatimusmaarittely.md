## Vaatimusmäärittely

> [!NOTE]
> Sijoita _vaatimusmaarittely.md_-tiedosto repositorioon _dokumentaatio_-hakemistoon ja lisää repositorion _README.md_-tiedostoon _vaatimusmaarittely.md_ -tiedostoon vievä linkki.

----

Ohjelman tarkoitus on tallentaa painiliikkeitä joita valmentajat voivat jakaa keskenään. Tietojen talennus tapahtuu lokaalisti markdown tiedostojen avulla.

### Käyttäjät
Sovelluksessa valmentajat ovat eri käyttäjiä. Lisäksi ohjelmassa voisi olla myös pääkäyttäjiä jotka pystyvät tekemään enemmän muutoksia ohjelman toimintaan.

### Perusversio: kurssin alkupuolen toteutus

Ennen kirjautumista:

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen ✅
    - Käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 3 merkkiä ✅
- Käyttäjä voi kirjautua järjestelmään ✅
    - Kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus ja salasana kirjautumislomakkeelle ✅
    - Jos käyttäjää ei olemassa, tai salasana ei täsmää, ilmoittaa järjestelmä tästä ✅
- Käyttäjä näkee kaikki painiliikkeet listana mutta ei voi luoda uusia ✅
- Käyttäjä pystyy tarkastelemaan yksittäisen liikkeen tietoja tekstimuodossa ✅

Kirjautumisen jälkeen:

- Käyttäjä voi luoda uuden painiliikkeen ✅
- Käyttäjä voi kirjautua ulos järjestelmästä ✅

Painiliikkeen talennus: ✅

Käyttöliittymässä pystyy asettamaan seuraavat metatiedot ✅
- nimi 
- kuva (ulkoinen linkki kuvaan)
- painimuoto (WW, FS, GR)
- ikäryhmä (6+, 12+, 16+)
- vaikeusaste (basic, intermediate, advanced)
- linkki (ulkoinen referenssi)
- lisäksi tallennus käyttää implisiittisiä metatietoja:
    - kuka on tehnyt tämän tallennuksen alunperin
    - milloin tallennus on tehty

### Laajennetut ominaisuudet
- painiliikkeiden editointi tai poisto ✅
- monivalinta elementit liikkeen tallennuksessa/muokkaamisessa
- liikkeen muokkaushistorian tarkastelu (kuka on muokannut ja milloin) ✅
- kuvien näyttäminen ShowMoveView-näkymässä
- kuvien näyttäminen listauksessa
- paikallisten kuvien käyttö
- listauksen järjestyksen muuttaminen
- tekstihaku
- haku metatietojen perusteella
- markdown tiedostojen renderöinti

Pääkäyttäjä:
- ikäryhmien lisääminen/muutto
- poistojen vahvistus

