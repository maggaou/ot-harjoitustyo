## Sovelluksen rakenne

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

### Päivitys (viikko 5)

Liikkeeseen tallennetaan [(str:päivämäärä,str:käyttäjä),..] muodossa muokkaushistoria, mutta varsinainen liikkeen ohjelmakoodi ei käytä User-luokkaa, vaan muokkaushistoria on pelkästään tekstiä.

## Toiminnallisuus / liikkeen luominen 

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant MovesService
    participant MovesRepository
    participant move
    User ->> UI: click "Create new"
    UI ->> MovesService: create_move(**args)
    MovesService ->> move: args["original_creator"] = self._user.username<br/>Move(**args)
    MovesService ->> MovesRepository: create(move)
    Note right of MovesRepository: move is now<br/>stored in the DB
    UI ->> UI: show_moves_view()
    UI ->> UI: MovesView.<br/>initialize_moves_list()
    Note right of UI: UI finds all moves<br/>from disk
    UI ->> MovesService: return_all()
    MovesService ->> MovesRepository: find_all()
    MovesRepository -->> UI: returns all moves
    UI ->> UI: MovesView.pack()
```
