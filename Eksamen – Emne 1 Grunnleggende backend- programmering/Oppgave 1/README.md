# Dyrepensjonat – Database

## Oppgave 1 – Opprettelse av database og datamodell

Databasen `dyrepensjonat` er opprettet i MySQL med utgangspunkt i ER-diagrammet i eksamensoppgaven.

Databasen består av fire tabeller:

- **owners** – Inneholder informasjon om dyreeierne, med navn, telefonnummer og e-postadresse.
- **pets** – Inneholder informasjon om kjæledyrene. Hvert kjæledyr er knyttet til én eier gjennom `owner_id`.
- **rooms** – Inneholder informasjon om rommene på pensjonatet, med romnummer, romtype og dagspris.
- **stays** – Registrerer oppholdene til kjæledyrene, med referanse til både kjæledyr og rom, samt innsjekks- og utsjekksdato.

## Nøkler og datatyper

Alle tabellene har en primærnøkkel (`PRIMARY KEY`) med `AUTO_INCREMENT`, slik at hver rad får en automatisk generert ID.

Fremmednøkler (`FOREIGN KEY`) er brukt for å koble sammen tabellene:

- `pets.owner_id` refererer til `owners.owner_id`.
- `stays.pet_id` refererer til `pets.pet_id`.
- `stays.room_id` refererer til `rooms.room_id`.

Det er brukt `INT` for ID-felter, `VARCHAR` for tekstfelt, `DATE` for datoer og `DECIMAL(8,2)` for romprisene. Obligatoriske felt er definert med `NOT NULL`. Romnummer er definert som unikt med `UNIQUE`.

## Eksempeldata

Det er lagt inn realistiske eksempeldata i alle tabellene:

- 5 eiere
- 5 rom
- 6 kjæledyr
- 5 opphold

## Kjøring av SQL-scriptet

SQL-scriptet `database.sql` oppretter databasen dersom den ikke finnes, oppretter tabellene og legger inn eksempeldata.

Eksisterende tabeller slettes før de opprettes på nytt. Dette gjøres for at scriptet skal kunne kjøres flere ganger uten manuell opprydding.

Scriptet er utviklet og testet i MySQL, og er kjørt på nytt uten feil.