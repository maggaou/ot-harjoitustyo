```mermaid
classDiagram
    User "1..*" -- "*" Move
    MovesService "0..1" -- "0..1" User
    MovesService "1" -- "1" UserRepository
    UserRepository "1" -- "*" User
    MovesRepository "1" -- "1" MovesService
    MovesRepository "1" -- "*" Move
```

Tällä hetkellä yhteen liikkeeseen liittyy vain yksi käyttäjä, mutta myöhemmin kaikki käyttäjät pystyisivät muokkaamaan mitä tahansa liikkeitä. Tällöin liike voisi tallentaa tiedon siitä, kuka on muokannut liikettä ja milloin.