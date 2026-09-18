Oppgave 4 – Filer, feilhåndtering og feilsøking

BESKRIVELSE

Programmet leser supporthenvendelser fra supporthenvendelser.csv, kontrollerer dataene og analyserer alle gyldige rader.

Ugyldige rader hoppes over. Programmet skriver en feilmelding i terminalen som viser radnummer og hva som er feil, og fortsetter med neste rad.

Programmet lager også support-rapport.txt hver gang det kjøres. Rapporten overskrives dersom den allerede finnes.


OPPGAVE 4.1 – LES OG KONTROLLER DATA

CSV-filen leses med csv.DictReader og åpnes med UTF-8-koding.

Filen åpnes med with open(...), slik at filen lukkes trygt etter bruk.

Hver rad kontrolleres for følgende:

id må være et positivt heltall.
category må ha en verdi.
minutes må være et heltall på null eller mer.
is_resolved må være nøyaktig yes eller no.
Alle feltene må ha en verdi.

Ugyldige rader hoppes over, og programmet fortsetter med neste rad.


OPPGAVE 4.2 – ANALYSE AV DATA

Bare gyldige rader brukes i analysen.

Programmet finner:

Antall gyldige henvendelser.
Antall henvendelser i hver kategori.
Samlet tidsbruk per kategori.
Gjennomsnittlig tidsbruk per kategori.
Antall løste henvendelser.
Antall uløste henvendelser.
Kategorien med flest henvendelser.
Uløste henvendelser sortert med den mest tidkrevende først.


OPPGAVE 4.3 – SKRIV RAPPORT

Programmet oppretter filen support-rapport.txt.

Filen opprettes dersom den ikke finnes, og overskrives dersom den finnes fra før.

Rapporten inneholder bare analysen av de gyldige radene.

Feilmeldinger om ugyldige CSV-rader skrives bare til terminalen og tas ikke med i rapporten.


OPPGAVE 4.4 – RETT FEILEN

Funksjonen sum_resolved_minutes() er rettet slik at minutes konverteres fra tekst til heltall før verdien legges sammen.

CSV-data som leses med csv.DictReader blir lest inn som tekst. Derfor vil request["minutes"] være en streng.

Denne koden ville gitt TypeError:

total += request["minutes"]

Riktig kode er:

total += int(request["minutes"])

int() gjør om teksten til et heltall før summeringen utføres.

Det brukes målrettet try/except i programmet. ValueError brukes ved konvertering av id og minutes, FileNotFoundError og OSError brukes ved filfeil, UnicodeDecodeError brukes ved feil tegnkoding, og csv.Error brukes ved feil under CSV-lesing. Det brukes ikke et tomt except som skjuler alle feil.


STANDARD BIBLIOTEK

Programmet bruker csv fra Python-standardbiblioteket for å lese CSV-filen.

Offisiell dokumentasjon:
https://docs.python.org/3/library/csv.html

Programmet bruker også pathlib for å finne CSV-filen og rapportfilen i samme mappe som programfilen.

Offisiell dokumentasjon:
https://docs.python.org/3/library/pathlib.html

Den innebygde funksjonen sorted() brukes til å sortere de uløste henvendelsene etter minutes, med mest tidkrevende først.

Offisiell dokumentasjon:
https://docs.python.org/3/library/functions.html


TESTING

Testene er utført med den medfølgende supporthenvendelser.csv.

Test 1
Gyldig id: 1
Forventet resultat: Raden godtas.
Resultat: Godkjent.

Test 2
Ugyldig minutes: thirty på rad 7.
Forventet resultat: Raden hoppes over og feilmelding vises i terminalen.
Resultat: Godkjent.

Test 3
Manglende category på rad 9.
Forventet resultat: Raden hoppes over og feilmelding vises i terminalen.
Resultat: Godkjent.

Test 4
Manglende minutes på rad 13.
Forventet resultat: Raden hoppes over og feilmelding vises i terminalen.
Resultat: Godkjent.

Test 5
Ugyldig is_resolved på rad 16: maybe.
Forventet resultat: Raden hoppes over og feilmelding vises i terminalen.
Resultat: Godkjent.

Test 6
Ugyldig id på rad 20: -19.
Forventet resultat: Raden hoppes over og feilmelding vises i terminalen.
Resultat: Godkjent.

Test 7
Gyldig løst henvendelse.
Forventet resultat: is_resolved = yes telles som løst.
Resultat: Godkjent.

Test 8
Gyldig uløst henvendelse.
Forventet resultat: is_resolved = no telles som uløst.
Resultat: Godkjent.

Test 9
Analyse av antall gyldige henvendelser.
Forventet resultat: 15 gyldige henvendelser.
Resultat: Godkjent.

Test 10
Analyse av kategori.
Forventet resultat: utstyr har flest henvendelser med 5.
Resultat: Godkjent.

Test 11
Sortering av uløste henvendelser.
Forventet resultat: ID 13, 4, 10, 2, 17 og 7 i denne rekkefølgen.
Resultat: Godkjent.


VERIFISERTE RESULTATER FRA CSV-FILEN

Antall gyldige henvendelser: 15
Antall løste henvendelser: 9
Antall uløste henvendelser: 6

Antall per kategori:
innlogging: 4
nettverk: 2
programvare: 4
utstyr: 5

Samlet tidsbruk per kategori:
innlogging: 53 minutter
nettverk: 62 minutter
programvare: 134 minutter
utstyr: 217 minutter

Gjennomsnittlig tidsbruk per kategori:
innlogging: 13.25 minutter
nettverk: 31.00 minutter
programvare: 33.50 minutter
utstyr: 43.40 minutter

Samlet tidsbruk for løste henvendelser: 184 minutter

Kategori med flest henvendelser: utstyr, 5 henvendelser

Uløste henvendelser, sortert med mest tidkrevende først:
ID 13: utstyr – 63 minutter
ID 4: utstyr – 55 minutter
ID 10: programvare – 48 minutter
ID 2: programvare – 42 minutter
ID 17: utstyr – 39 minutter
ID 7: nettverk – 35 minutter


EKSEMPEL PÅ FEILMELDINGER I TERMINALEN

Rad 7 er ugyldig: minutes må være et heltall
Rad 9 er ugyldig: feltet 'category' mangler verdi
Rad 13 er ugyldig: feltet 'minutes' mangler verdi
Rad 16 er ugyldig: is_resolved må være nøyaktig 'yes' eller 'no'
Rad 20 er ugyldig: id må være et positivt heltall


LEVERANSER

oppgave-4.py
supporthenvendelser.csv
support-rapport.txt
README.md
