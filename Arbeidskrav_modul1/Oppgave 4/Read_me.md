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
CSV-data som leses med csv. DictReader blir lest inn som tekst. Derfor vil request["minutes"] være en streng.
Denne koden ville gitt TypeError:

total += request["minutes"]

Riktig kode er:
total += int(request["minutes"])
int() gjør om teksten til et heltall før summeringen utføres.
Det brukes målrettet try/except i programmet. 
ValueError brukes ved konvertering av id og minutes, 
FileNotFoundError og OSError brukes ved filfeil, 
UnicodeDecodeError brukes ved feil tegnkoding, 
csv.Error brukes ved feil under CSV-lesing. Det brukes ikke et tomt except som skjuler alle feil.


STANDARDLIBRARY OG DOKUMENTASJON

Programmet bruker Python-standardbiblioteket csv for lesing og skriving av CSV-filer og datetime for håndtering av datoer.

Offisiell dokumentasjon for csv:
https://docs.python.org/3/library/csv.html

Offisiell dokumentasjon for datetime:
https://docs.python.org/3/library/datetime.html


