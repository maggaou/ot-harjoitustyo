## Vaatimusmäärittely

Ohjelman tarkoitus on tallentaa painiliikkeitä joita valmentajat voivat jakaa keskenään. Liikkeiden talennus tapahtuu tekstitiedostojen avulla jotka sisältävät YAML-metatieto osion.

### Käyttäjät
Sovelluksessa valmentajat ovat eri käyttäjiä.

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
- kuvien näyttäminen ShowMoveView-näkymässä ✅
- näytä relevantit virheilmoitukset liikkeen luonnissa/muokkauksessa ✅
- listauksen järjestyksen muuttaminen ✅
