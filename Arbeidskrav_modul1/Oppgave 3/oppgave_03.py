from datetime import datetime, timedelta

# Oppgave 3

# Starter med å definere noen funksjoner som jeg bruker senere.


def Read_date(date_text):
    # Leser inn dato (dd.mm.åååå) og returnerer den.
    date = datetime.strptime(date_text, "%d.%m.%Y")
    return date


def Read_time():
    #Leser inn et gyldig starttidspunkt på (tt:mm).
    while True:
        time_text = input("Skriv inn starttidspunkt (tt:mm): ")

        try:
            time = datetime.strptime(time_text, "%H:%M")
            return time
        except ValueError:
            print("Ugyldig tidspunkt! Bruk formatet tt:mm.")


def Combine_date(dato, tidspunkt):
    # Slår sammen dato og tid fra over til en felles variabel
    start = datetime.combine(dato.date(), tidspunkt.time())
    return start


def Calc_end(start, minutter):
    # Ut fra start + minutter så returnere slutt
    end = start + timedelta(minutes=minutter)
    return end


def Days_between(start, slutt):
    # Beregner dager mellom og returnere det som et positivt tall
    days = abs((slutt - start).days)
    return days


def Sorted_date(datoer):
    # Sorterer datoer ut fra en liste med datoer, returnerer en sortert liste
    sorted_dates = sorted(datoer)
    return sorted_dates


# Selve programmet.

print("\n--- PLANLEGGING AV STUDIEØKT ---")

# Start dato
while True:
    date_text = input("Skriv inn dato (dd.mm.åååå): ")

    try:
        start_date = Read_date(date_text)
        break
    except ValueError:
        print("Ugyldig dato! Bruk formatet dd.mm.åååå.")


start_time = Read_time()
start_date_time = Combine_date(start_date, start_time)


# Studie tid
while True:
    try:
        minutes = int(input("Hvor lenge skal du studere? "))

        if minutes > 0:
            break
        else:
            print("Varigheten må være et positivt heltall.")

    except ValueError:
        print("Du må skrive inn et heltall.")

end_time = Calc_end(start_date_time, minutes)



# Dato 2, ref punkt om å regne dager mellom

while True:
    calc_date_text = input("Skriv inn en annen dato for å beregne dager mellom (dd.mm.åååå): ")

    try:
        calc_date = Read_date(calc_date_text)
        break
    except ValueError:
        print("Ugyldig dato! Bruk formatet dd.mm.åååå.")


days_between = Days_between(start_date, calc_date)


# Dato 3, ref punkt om å ta imot en liste med datoer.

dates = []

print("\n--- DATOER TIL SORTERING ---")
print("Skriv inn flere datoer.")
print("Trykk Enter uten tekst når du er ferdig.")

while True:
    date_list_text = input("Dato (dd.mm.åååå): ")

    # Tom input avslutter innleggingen
    if date_list_text == "":
        break

    try:
        date_list = Read_date(date_list_text)
        dates.append(date_list)

    except ValueError:
        print("Ugyldig dato! Bruk formatet dd.mm.åååå.")


# Sorter listen
sorted_dates = Sorted_date(dates)


# Resultat av oppgaven.

print("\n--- RESULTATER ---")

print(f"Start: {start_date_time.strftime('%d.%m.%Y %H:%M')}")
print(f"Slutt: {end_time.strftime('%d.%m.%Y %H:%M')}")
print(f"Varighet: {minutes} minutter")
print(f"Dager mellom datoene: {days_between}")
print("\nSorterte datoer:")

if len(sorted_dates) == 0:
    print("Ingen datoer ble lagt inn.")
else:
    for dato in sorted_dates:
        print(dato.strftime("%d.%m.%Y"))