# Moves
Ohjelman tarkoitus on tallentaa painiliikkeitä joita valmentajat voivat jakaa keskenään. Tietojen talennus tapahtuu lokaalisti markdown tiedostojen avulla.

## Releases
- [Viikko 5](https://github.com/maggaou/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/maggaou/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](https://github.com/maggaou/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](https://github.com/maggaou/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/maggaou/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

## Asennus
Projektin juuressa:
- riippuvuuksien asennus `poetry install`
- virtuaaliympäristön aktivointi `eval $(poetry env activate)`
- tietokannan alustus `invoke build`
- käynnistys `invoke start`

## invoke-komennot
Katso komennot suorittamalla `invoke --list`. Suorita komento invoken avulla `invoke <komento>`. 

invoke-komennot:
- ohjelman suorittaminen: **start**
- liikkeiden poisto: **clear-moves**
- testikattavuusraportti/coverage: **coverage-report**
- aja autopep8: **format-with-autopep8**
- aja pylint: **lint**
- avaa repo-sivu: **repo-github**
- tietokannan alustus: **reset-database**
- näytä tietokannan käyttäjät: **show-users**
- aja pytest: **test**
