# Diagramme De Sequence List

```mermaid
sequenceDiagram
    participant User
    participant API
    participant BusinessLogic
    participant Database

    User->>API: POST /List of Places (Criteria: Location, Price, )
    API->>BusinessLogic: validateListOfPlaces(Criteria)
    BusinessLogic->>Database: fetchPlaces(criteria)
    Database-->>BusinessLogic: Places found? (List of places/empty)
    alt No places found
        BusinessLogic-->>API: NoPlacesFoundError()
        API-->>User: 404 Not Found (No places matching criteria)
    else Places found
        BusinessLogic->>Database: insertUser(username, email, hashedPassword)
        Database-->>BusinessLogic: User inserted (user_id)
        BusinessLogic-->>API: userCreated/Error (user_id, email, password)
        API-->>User: 201 Created (user_id, welcome message) <br />400 (Data Error)
    end
```

Cliquez sur ce lien pour consulter le diagramme: [Mermaid Live Editor](https://www.mermaidchart.com/play?utm_source=mermaid_live_editor&utm_medium=banner_ad&utm_campaign=visual_editor#pako:eNp9UU1Lw0AQ_StDTim0JEpPQSraKgilDai3gkw3k3Qh2Y27G4uI_93dNEkbE80hh5n3NW-_PCYT8iJP03tFgtGKY6aw2KmdAPuVqAxnvERh4FWTGpvfxU9j4_tKc0Far2XG2RhghQb3qMnt2r3zmC0WVjKCePv8AsGaawMyhThHRhr8peKGFMcI1pKh4VJMIVac0RQmrYqlW5FegAg-MOcJGnKC2_Qk16l11B7JirQhI0jJsENDY79pLWw29G2Cp7ISyS347T1lPQ6oKM1nJ4O5gY1sdidKuxqGa3vayJPFo4M_KCWVP7lkuTYs1lUbwTycW4KBGgz-2axAex4XGQxuo1xT74q_I132xYU1NM7Vr-xPYGGfiArk-RQOqA-UxKj1Uaqkl_afJp1WI0s2u1N94332eEMOuVRkHz8J6oI6cpeoHMvSa-46vIJG5IJ-pJzJgqCwppjRBG72CoLFPAzBd6dA7XfuUiTe9w-kKycA)
