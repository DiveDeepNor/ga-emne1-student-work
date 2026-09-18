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
Datafilen som brukes til lagring. Dersom filen ikke finnes når programmet startes, opprettes den automatisk med kolonneoverskrifter og en tom samling.

aktiviteter-eksempel.csv
Eksempeldata som kan kopieres over til aktiviteter.csv for å starte med ferdige testdata.

README.md
Dokumentasjon av programmet.

GIT-OPPSKRIFT.txt
Forslag til meningsfulle Git-commits og enkel arbeidsflyt.


KLASSE

Aktivitet-klassen representerer én aktivitet.

Attributter:
title
category
date
estimated_minutes
status

Metoden mark_completed() endrer status fra planned til completed.

Programmet bruker ikke arv eller annen avansert objektorientering. Klassen er holdt på introduksjonsnivå.


FUNKSJONER

les_tekst()
Leser inn tekst og kontrollerer at feltet ikke er tomt.

les_dato()
Leser inn en gyldig dato på formatet dd.mm.åååå.

les_positivt_heltall()
Kontrollerer at estimert varighet er et positivt heltall.

les_status()
Kontrollerer at status er planned eller completed.

vis_aktiviteter()
Viser aktivitetene på en oversiktlig måte.

registrer_aktivitet()
Leser inn en aktivitet, oppretter et Aktivitet-objekt og legger det i aktivitetslisten.

filtrer_kategori()
Søker etter tekst i kategori og viser aktivitetene som passer.

filtrer_status()
Viser aktiviteter med valgt status.

sorter_aktiviteter()
Sorterer aktivitetene etter dato eller estimert varighet.

marker_fullfort()
Viser planlagte aktiviteter og lar brukeren velge én som skal markeres som completed.

vis_statistikk()
Viser totalt antall aktiviteter, samlet estimert tid og antall fullførte aktiviteter.

opprett_datafil()
Oppretter CSV-filen med riktige kolonneoverskrifter.

aktivitet_til_rad()
Gjør et Aktivitet-objekt om til data som kan skrives til CSV.

rad_til_aktivitet()
Kontrollerer en CSV-rad og gjør den om til et Aktivitet-objekt.

lagre_aktiviteter()
Skriver aktivitetene til CSV-filen.

les_aktiviteter()
Leser aktivitetene fra CSV-filen. Ugyldige rader hoppes over med en forklaring.

lagre_og_les_aktiviteter()
Lagrer aktivitetene og leser dem deretter inn igjen.

vis_meny()
Skriver ut menyen.

les_menyvalg()
Validerer at menyvalget er mellom 1 og 8.

main()
Styrer hovedprogrammet og kaller riktig funksjon.


DATAFIL

CSV ble valgt som filformat fordi CSV er enkelt å lese og skrive i Python og fordi CSV ble brukt i Oppgave 4.

Datafilen har følgende kolonner:

title
category
date
estimated_minutes
status

Dato lagres som dd.mm.åååå.

Eksempel:

title,category,date,estimated_minutes,status
Python,Programmering,18.09.2026,90,planned


BRUK

Start programmet med:

python oppgave-5.py

Ved første oppstart, hvis aktiviteter.csv ikke finnes, opprettes filen automatisk. Programmet viser en forståelig melding og fortsetter med en tom aktivitetsliste.

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

Programmet lagrer ikke automatisk etter hvert valg. Brukeren lagrer og leser data tilbake med menyvalg 7. Dette gjør lagring og innlesing tydelig som en del av programflyten.

Ved ugyldig input stopper ikke programmet. Brukeren får en forklaring og får prøve på nytt.


TESTING

Test 1 – registrere aktivitet

Input:
Tittel: Python
Kategori: Programmering
Dato: 18.09.2026
Estimert tid: 90

Forventet:
Aktiviteten registreres med status planned og vises i aktivitetslisten.

Resultat:
Godkjent.


Test 2 – tomt tekstfelt

Input:
Trykk Enter som tittel.

Forventet:
Programmet viser feilmelding og spør etter tittel på nytt.

Resultat:
Godkjent.


Test 3 – ugyldig dato

Input:
31.02.2026

Forventet:
Programmet viser feilmelding og spør etter dato på nytt.

Resultat:
Godkjent.


Test 4 – ugyldig varighet

Input:
abc

Forventet:
Programmet viser feilmelding og spør etter et positivt heltall.

Resultat:
Godkjent.


Test 5 – null og negativ varighet

Input:
0
eller
-20

Forventet:
Programmet viser feilmelding og spør etter positiv varighet.

Resultat:
Godkjent.


Test 6 – ugyldig menyvalg

Input:
9

Forventet:
Programmet viser feilmelding og viser menyen på nytt.

Resultat:
Godkjent.


Test 7 – filtrere kategori

Registrer aktiviteter i forskjellige kategorier og velg menyvalg 2.

Forventet:
Bare aktiviteter som passer den innskrevne kategorien vises.

Resultat:
Godkjent.


Test 8 – filtrere status

Marker en aktivitet som fullført og velg menyvalg 3.

Forventet:
Aktiviteter med valgt status vises.

Resultat:
Godkjent.


Test 9 – sortere

Registrer aktiviteter med forskjellige datoer og varigheter og velg menyvalg 4.

Forventet:
Ved valg 1 sorteres datoene med eldste først.
Ved valg 2 sorteres varighet med lengst først.

Resultat:
Godkjent.


Test 10 – markere fullført

Velg menyvalg 5 og velg en planlagt aktivitet.

Forventet:
Status endres fra planned til completed.

Resultat:
Godkjent.


Test 11 – statistikk

Registrer flere aktiviteter med kjente varigheter og marker noen som fullført. Velg menyvalg 6.

Forventet:
Totalt antall aktiviteter, samlet estimert tid og antall fullførte vises korrekt.

Resultat:
Godkjent.


Test 12 – lagre og lese

Registrer aktiviteter og velg menyvalg 7.

Forventet:
Aktivitetene skrives til aktiviteter.csv og leses deretter inn igjen.

Resultat:
Godkjent.


Test 13 – manglende datafil

Slett aktiviteter.csv før oppstart.

Forventet:
Programmet oppretter en ny tom datafil, viser en melding i terminalen og fortsetter med tom aktivitetsliste.

Resultat:
Godkjent.


Test 14 – ugyldig rad i datafil

Legg inn en CSV-rad med ugyldig dato, negativ varighet eller ugyldig status.

Forventet:
Programmet viser hvilken rad som hoppes over og fortsetter med resten av dataene.

Resultat:
Godkjent.


Test 15 – data beholdes etter ny kjøring

Lagre aktiviteter, avslutt programmet, start det på nytt og velg menyvalg 1 eller 3.

Forventet:
De tidligere lagrede aktivitetene er tilgjengelige.

Resultat:
Godkjent.


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


OPPFYLLELSE AV OPPGAVETEKSTEN

Programmet har:

En klasse som heter Aktivitet.
Attributtene title, category, date, estimated_minutes og status.
Minst én metode i Aktivitet-klassen.
Flere hensiktsmessige funksjoner i tillegg til klassemetoden.
En liste som inneholder aktivitetene.
En nummerert meny som vises på nytt etter hvert valg.
Registrering og visning av aktiviteter.
Filtrering på kategori.
Filtrering på status.
Sortering etter dato eller varighet.
Mulighet til å markere aktiviteter som completed.
Statistikk for antall aktiviteter, samlet estimert tid og antall fullførte.
Lagring til datafil og innlesing igjen.
Opprettelse av datafil ved første oppstart dersom den mangler.
Validering av menyvalg, tom tekst, dato og varighet.
Forståelige feilmeldinger.
Dokumentasjon med valg, tester, kjente begrensninger og forbedringsmuligheter.


MERK OM GIT

Oppgaven krever Git og flere meningsfulle commits. Filen GIT-OPPSKRIFT.txt inneholder et forslag til commitrekkefølge.

Git-arbeidsflyten bør gjøres i studentens eget repository:

git clone <repository>
git add oppgave-5.py aktiviteter.csv README.md
git commit -m "Lag aktivitet og grunnmeny"
git add .
git commit -m "Legg til filtrering, sortering og statistikk"
git add .
git commit -m "Legg til CSV-lagring og feilhåndtering"
git add .
git commit -m "Oppdater tester og dokumentasjon"
git push

Commit-meldingene må tilpasses det som faktisk er gjort i prosjektet.
