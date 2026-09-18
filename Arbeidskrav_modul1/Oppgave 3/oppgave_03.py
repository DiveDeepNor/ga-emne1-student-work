from datetime import datetime, timedelta


# --------------------------------------------------
# FUNKSJONER
# --------------------------------------------------

def les_dato(dato_tekst):
    """Tar imot en dato som tekst på formatet dd.mm.åååå og returnerer datetime."""
    dato = datetime.strptime(dato_tekst, "%d.%m.%Y")
    return dato


def les_tidspunkt():
    """Leser inn et gyldig starttidspunkt på formatet tt:mm."""
    while True:
        tidspunkt_tekst = input("Skriv inn starttidspunkt (tt:mm): ")

        try:
            tidspunkt = datetime.strptime(tidspunkt_tekst, "%H:%M")
            return tidspunkt
        except ValueError:
            print("Ugyldig tidspunkt! Bruk formatet tt:mm.")


def kombiner_dato(dato, tidspunkt):
    """Kombinerer dato og klokkeslett til ett datetime-objekt."""
    start = datetime.combine(dato.date(), tidspunkt.time())
    return start


def beregn_slutt(start, minutter):
    """Tar imot starttidspunkt og minutter og returnerer sluttidspunkt."""
    slutt = start + timedelta(minutes=minutter)
    return slutt


def dager_mellom(start, slutt):
    """Returnerer positivt antall hele dager mellom to datoer."""
    dager = abs((slutt - start).days)
    return dager


def sorter_datoer(datoer):
    """Tar imot en liste med datoer og returnerer en kronologisk sortert liste."""
    sorterte_datoer = sorted(datoer)
    return sorterte_datoer


# --------------------------------------------------
# HOVEDPROGRAM
# --------------------------------------------------

print("\n--- PLANLEGGING AV STUDIEØKT ---")


# --------------------------------------------------
# STARTDATO
# --------------------------------------------------

while True:
    dato_tekst = input("Skriv inn dato (dd.mm.åååå): ")

    try:
        start_dato = les_dato(dato_tekst)
        break
    except ValueError:
        print("Ugyldig dato! Bruk formatet dd.mm.åååå.")


# --------------------------------------------------
# STARTTIDSPUNKT
# --------------------------------------------------

start_tid = les_tidspunkt()

start_tidspunkt = kombiner_dato(start_dato, start_tid)


# --------------------------------------------------
# VARIGHET
# --------------------------------------------------

while True:
    try:
        minutter = int(input("Hvor lenge skal du studere? "))

        if minutter > 0:
            break
        else:
            print("Varigheten må være et positivt heltall.")

    except ValueError:
        print("Du må skrive inn et heltall.")


# --------------------------------------------------
# BEREGN SLUTTID
# --------------------------------------------------

slutt_tidspunkt = beregn_slutt(start_tidspunkt, minutter)


# --------------------------------------------------
# ANDRE DATO
# Brukes til funksjonen dager_mellom()
# --------------------------------------------------

while True:
    dato_2_tekst = input("Skriv inn en annen dato for å beregne dager mellom (dd.mm.åååå): ")

    try:
        dato_2 = les_dato(dato_2_tekst)
        break
    except ValueError:
        print("Ugyldig dato! Bruk formatet dd.mm.åååå.")


dager_i_mellom = dager_mellom(start_dato, dato_2)


# --------------------------------------------------
# FLERE DATOER TIL SORTERING
# --------------------------------------------------

datoer = []

print("\n--- DATOER TIL SORTERING ---")
print("Skriv inn flere datoer.")
print("Trykk Enter uten tekst når du er ferdig.")

while True:
    dato_liste_tekst = input("Dato (dd.mm.åååå): ")

    # Tom input avslutter innleggingen
    if dato_liste_tekst == "":
        break

    try:
        dato_liste = les_dato(dato_liste_tekst)
        datoer.append(dato_liste)

    except ValueError:
        print("Ugyldig dato! Bruk formatet dd.mm.åååå.")


# Sorter listen
sorterte_datoer = sorter_datoer(datoer)


# --------------------------------------------------
# RESULTATER
# --------------------------------------------------

print("\n--- RESULTATER ---")

print(f"Start: {start_tidspunkt.strftime('%d.%m.%Y %H:%M')}")
print(f"Slutt: {slutt_tidspunkt.strftime('%d.%m.%Y %H:%M')}")
print(f"Varighet: {minutter} minutter")
print(f"Dager mellom datoene: {dager_i_mellom}")


print("\nSorterte datoer:")

if len(sorterte_datoer) == 0:
    print("Ingen datoer ble lagt inn.")
else:
    for dato in sorterte_datoer:
        print(dato.strftime("%d.%m.%Y"))