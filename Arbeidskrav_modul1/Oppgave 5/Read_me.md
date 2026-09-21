Oppgave 5 – Miniprosjekt: aktivitetsplanlegger

BESKRIVELSE

Programmet er et konsollbasert program for planlegging og oppfølging av aktiviteter.

En aktivitet har attributtene:

title
category
date
estimated_minutes
status

Status kan være planned eller completed.

Programmet viser en nummerert meny i terminalen. Menyen vises på nytt etter hvert valg, bortsett fra når brukeren velger å avslutte.


FILSTRUKTUR

oppgave-5.py
Hovedprogrammet med Aktivitet-klassen, funksjoner og meny.

aktiviteter.csv
Datafilen som brukes til lagring. 
Dersom filen ikke finnes når programmet startes, opprettes den automatisk med kolonneoverskrifter og en tom samling.

aktiviteter-eksempel.csv
Eksempeldata som kan kopieres over til aktiviteter.csv for å starte med ferdige testdata.

README.md
Dokumentasjon av programmet




KLASSE

Aktivitet-klassen representerer én aktivitet.

Attributter:
title
category
date
estimated_minutes
status

Metoden mark_completed() endrer status fra planned til completed.



FUNKSJONER

read_text()
Leser inn tekst og kontrollerer at feltet ikke er tomt.

read_dato()
Leser inn en gyldig dato på formatet dd.mm.åååå.

read_pos_integer()
Kontrollerer at estimert varighet er et positivt heltall.

read_status()
Kontrollerer at status er planned eller completed.

show_activitys()
Viser aktivitetene på en oversiktlig måte.

register_activity()
Leser inn en aktivitet, oppretter et Aktivitet-objekt og legger det i aktivitetslisten.

filt_Category()
Søker etter tekst i kategori og viser aktivitetene som passer.

filt_status()
Viser aktiviteter med valgt status.

sort_activitys()
Sorterer aktivitetene etter dato eller estimert varighet.

mark_completed()
Viser planlagte aktiviteter og lar brukeren velge én som skal markeres som completed.

show_stats()
Viser totalt antall aktiviteter, samlet estimert tid og antall fullførte aktiviteter.

create_datafile()
Oppretter CSV-filen med riktige kolonneoverskrifter.

aktivity_to_row()
Gjør et Aktivitet-objekt om til data som kan skrives til CSV.

row_to_aktivity()
Kontrollerer en CSV-rad og gjør den om til et Aktivitet-objekt.

save_aktivity()
Skriver aktivitetene til CSV-filen.

show_aktivity()
Leser aktivitetene fra CSV-filen. Ugyldige rader hoppes over med en forklaring.

save_and_read_activity()
Lagrer aktivitetene og leser dem deretter inn igjen.

show_menu()
Skriver ut menyen.

read_menuchoice()
Validerer at menyvalget er mellom 1 og 8.

main()
Styrer hovedprogrammet og kaller riktig funksjon.



Eksempel:

title,category,date,estimated_minutes,status
Python,Programmering,18.09.2026,90,planned


BRUK

Ved første oppstart, hvis aktiviteter.csv ikke finnes, opprettes filen automatisk. 
Programmet viser en melding og fortsetter med en tom aktivitetsliste.

Menyvalg:

1. Registrere og vise aktiviteter
2. Søke etter eller filtrere kategori
3. Filtrere etter status
4. Sortere etter dato eller varighet
5. Markere en aktivitet som fullført
6. Vise antall aktiviteter, samlet estimert tid og antall fullførte
7. Lagre aktiviteter til fil og lese dem inn igjen
8. Avslutte programmet


VALG SOM ER GJORT

Aktivitet er laget som en klasse fordi oppgaven krever en klasse med faste attributter og minst én metode.

Aktivitetene oppbevares i en liste.

CSV er valgt som datafil fordi det er et enkelt tekstformat og passer godt til aktivitetsdataene.

Nye aktiviteter får status planned.

Programmet lagrer ikke automatisk etter hvert valg. 
Brukeren lagrer og leser data tilbake med menyvalg 7. 
Dette gjør lagring og innlesing tydelig som en del av programflyten.

Ved ugyldig input stopper ikke programmet. Brukeren får en forklaring og får prøve på nytt.


TESTING

Test 1 – registrere aktivitet
Tittel: Python
Kategori: Programmering
Dato: 18.09.2026
Estimert tid: 90
Forventet:
Aktiviteten registreres med status planned og vises i aktivitetslisten.
Resultat: Godkjent.

Test 2 – tomt tekstfelt
Trykk Enter som tittel.
Forventet: Programmet viser feilmelding og spør etter tittel på nytt.
Resultat: Godkjent.

Test 3 – ugyldig dato
Input:31.02.2026
Forventet: Programmet viser feilmelding og spør etter dato på nytt.
Resultat: Godkjent.

Test 4 – ugyldig varighet
Input: abc
Forventet: Programmet viser feilmelding og spør etter et positivt heltall.
Resultat: Godkjent.

Test 5 – null og negativ varighet
Input: 0 eller -20
Forventet: Programmet viser feilmelding og spør etter positiv varighet.
Resultat: Godkjent.


KJENTE BEGRENSNINGER

Programmet har ikke funksjon for å slette eller redigere en aktivitet.
Programmet bruker én lokal CSV-fil.
Programmet er laget for enkel bruk fra terminalen.


MULIGE FORBEDRINGER

Det kan legges til funksjon for å redigere og slette aktiviteter.
Det kan legges til søk etter aktivitetstittel.
Det kan legges til filtrering på flere kriterier samtidig.
Det kan legges til automatisk lagring etter endringer.
Det kan legges til bedre visning av dato og tid.


STANDARDLIBRARY OG DOKUMENTASJON

Programmet bruker Python-standardbiblioteket csv for lesing og skriving av CSV-filer og datetime for håndtering av datoer.

Offisiell dokumentasjon for csv:
https://docs.python.org/3/library/csv.html

Offisiell dokumentasjon for datetime:
https://docs.python.org/3/library/datetime.html


