import csv
from datetime import datetime

# Oppgave 5

# Leser inn CSV og format

datafil = "aktiviteter.csv"
date_format = "%d.%m.%Y"


class Activity:
    # Representerer én aktivitet i aktivitetsplanleggeren

    def __init__(self, title, category, date, estimated_minutes, status="planned"):
        self.title = title
        self.category = category
        self.date = date
        self.estimated_minutes = estimated_minutes
        self.status = status

    def mark_completed(self):
        # Markerer aktiviteten som fullført
        self.status = "completed"


def Read_text(prompt):
    # Leser inn tekst og sjekker at feltet ikke er tomt
    while True:
        text = input(prompt).strip()

        if text:
            return text

        print("Feltet kan ikke være tomt. Prøv igjen.")


def Read_date(prompt):
    # Leser inn en dato på (dd.mm.åååå)
    while True:
        date_text = input(prompt).strip()

        try:
            return datetime.strptime(date_text, date_format)
        except ValueError:
            print("Ugyldig dato. Bruk formatet dd.mm.åååå.")


def Read_pos_integer(prompt):
    # Leser inn et positivt heltall
    while True:
        value_text = input(prompt).strip()

        try:
            value = int(value_text)

            if value > 0:
                return value

            print("Verdien må være et positivt heltall.")

        except ValueError:
            print("Du må skrive inn et positivt heltall.")


def Read_status(prompt="Status (planned/completed): "):
    # Leser inn en status og sjekker om den er gyldig.
    while True:
        status = input(prompt).strip().lower()

        if status in ("planned", "completed"):
            return status

        print("Ugyldig status. Skriv planned eller completed.")


def Show_activity(activity):
    # Viser aktiviteter på en oversiktlig måte.
    if not activity:
        print("Ingen aktiviteter å vise.")
        return

    for number, activity in enumerate(activity, start=1):
        print(
            f"{number}. {activity.title} | "
            f"{activity.category} | "
            f"{activity.date.strftime(date_format)} | "
            f"{activity.estimated_minutes} min | "
            f"{activity.status}"
        )


def Register_activity(activitys):
    # Registrerer ny aktivitet og viser aktivitetslisten
    print("\n--- REGISTRER AKTIVITET ---")

    title = Read_text("Tittel: ")
    category = Read_text("Kategori: ")
    date = Read_date("Dato (dd.mm.åååå): ")
    estimated_minutes = Read_pos_integer("Estimert tid i minutter: ")

    activity = Activity(
        title,
        category,
        date,
        estimated_minutes
    )

    activitys.append(activity)

    print("Aktiviteten er registrert.")
    print("\n--- AKTIVITETER ---")
    Show_activity(activitys)


def Filt_categories(activitys):
    # Søker etter tekst i aktivitetskategorien, for å filtrere på denne
    if not activitys:
        print("Ingen aktiviteter registrert.")
        return

    keyword = Read_text("Skriv inn kategori du vil søke etter: ").lower()

    result = [
        activity
        for activity in activitys
        if keyword in activity.category.lower()
    ]

    if not result:
        print("Ingen aktiviteter funnet i denne kategorien.")
        return

    print("\n--- RESULTAT ---")
    Show_activity(result)


def Filt_status(activitys):
    # Viser aktiviteter med status man ønsker
    if not activitys:
        print("Ingen aktiviteter registrert.")
        return

    status = Read_status()

    result = [
        activity
        for activity in activitys
        if activity.status == status
    ]

    if not result:
        print(f"Ingen aktiviteter med status '{status}'.")
        return

    print("\n--- RESULTAT ---")
    Show_activity(result)


def Sort_activitys(activitys):
    # Sorterer aktiviteter etter dato eller estimert varighet
    if not activitys:
        print("Ingen aktiviteter registrert.")
        return

    while True:
        choice = input(
            "Sorter etter 1 = dato (eldste først), "
            "2 = varighet (lengst først): "
        ).strip()

        if choice in ("1", "2"):
            break

        print("Ugyldig valg. Skriv 1 eller 2.")

    if choice == "1":
        sorted_activitys = sorted(activitys, key=lambda activity: activity.date)
    else:
        sorted_activitys = sorted(
            activitys,
            key=lambda activity: activity.estimated_minutes,
            reverse=True
        )

    print("\n--- SORTERTE AKTIVITETER ---")
    Show_activity(sorted_activitys)


def Mark_completed(activitys):
    # Sette en planlagt aktivitet som fullført
    planed = [
        activity
        for activity in activitys
        if activity.status == "planned"
    ]

    if not planed:
        print("Ingen planlagte aktiviteter å markere som fullført.")
        return

    print("\n--- PLANLAGTE AKTIVITETER ---")
    Show_activity(planed)

    while True:
        choice = input("Velg nummeret på aktiviteten som skal fullføres: ").strip()

        try:
            number = int(choice)

            if 1 <= number <= len(planed):
                planed[number - 1].mark_completed()
                print("Aktiviteten er markert som fullført.")
                return

            print("Nummeret finnes ikke. Prøv igjen.")

        except ValueError:
            print("Du må skrive inn et helt tall.")


def Show_stats(activitys):
    # Viser antall aktiviteter, samlet estimert tid og antall fullførte
    number_of_activities = len(activitys)

    total_time = sum(
        activity.estimated_minutes
        for activity in activitys
    )

    number_completed = sum(
        1
        for activity in activitys
        if activity.status == "completed"
    )

    print("\n--- STATISTIKK ---")
    print(f"Antall aktiviteter: {number_of_activities}")
    print(f"Samlet estimert tid: {total_time} minutter")
    print(f"Antall fullførte: {number_completed}")


def Create_datafile():
    # Lager en tom CSV-fil med riktig overskriftsrader
    with open(datafil, "w", newline="", encoding="utf-8") as fil:
        writer = csv.DictWriter(
            fil,
            fieldnames=[
                "title",
                "category",
                "date",
                "estimated_minutes",
                "status"
            ]
        )
        writer.writeheader()


def Activity_to_row(activity):
    # Gjør en aktivitet om til en dictionary for CSV filen
    return {
        "title": activity.title,
        "category": activity.category,
        "date": activity.date.strftime(date_format),
        "estimated_minutes": str(activity.estimated_minutes),
        "status": activity.status
    }


def Row_to_activity(row):
    # Gjør en rad om til en aktivitet
    title = (row.get("title") or "").strip()
    category = (row.get("category") or "").strip()
    date_tekst = (row.get("date") or "").strip()
    minutes_tekst = (row.get("estimated_minutes") or "").strip()
    status = (row.get("status") or "").strip().lower()

    if not title:
        raise ValueError("tittel mangler")

    if not category:
        raise ValueError("kategori mangler")

    try:
        date = datetime.strptime(date_tekst, date_format)
    except ValueError:
        raise ValueError("ugyldig dato")

    try:
        estimated_minutes = int(minutes_tekst)
    except ValueError:
        raise ValueError("estimert tid må være et heltall")

    if estimated_minutes <= 0:
        raise ValueError("estimert tid må være positiv")

    if status not in ("planned", "completed"):
        raise ValueError("status må være planned eller completed")

    return Activity(
        title,
        category,
        date,
        estimated_minutes,
        status
    )


def Save_activity(activitys):
    # Lagrer alle aktiviteter til CSV filen
    try:
        with open(datafil, "w", newline="", encoding="utf-8") as fil:
            writer = csv.DictWriter(
                fil,
                fieldnames=[
                    "title",
                    "category",
                    "date",
                    "estimated_minutes",
                    "status"
                ]
            )

            writer.writeheader()

            for activity in activitys:
                writer.writerow(Activity_to_row(activity))

        return True

    except OSError as error:
        print(f"Kunne ikke lagre datafilen: {error}")
        return False


def Read_activity():
    # Leser aktiviteter fra CSV filen
    try:
        with open(datafil, "r", newline="", encoding="utf-8") as fil:
            reader = csv.DictReader(fil)

            expexted_fields = {
                "title",
                "category",
                "date",
                "estimated_minutes",
                "status"
            }

            if reader.fieldnames is None or not expexted_fields.issubset(
                set(reader.fieldnames)
            ):
                print("Datafilen har feil format. Starter med en tom samling.")
                return []

            activitys = []

            for row_nr, row in enumerate(reader, start=2):
                try:
                    activity = Row_to_activity(row)
                    activitys.append(activity)
                except ValueError as error:
                    print(f"Rad {row_nr} ble hoppet over: {error}.")

            return activitys

    except (OSError, csv.Error) as error:
        print(f"Kunne ikke lese datafilen: {error}")
        print("Programmet fortsetter med en tom samling.")
        return []


def Save_and_read_activitys(activitys):
    # Lagrer aktivitetene og leser dem inn igjen
    if not Save_activity(activitys):
        return activitys

    print("Aktivitetene er lagret til datafilen.")

    loaded_activities = Read_activity()
    print("Aktivitetene er lest inn igjen fra datafilen.")

    return loaded_activities


def Show_menu():
    # Viser hovedmenyen
    print("\n--- MENY ---")
    print("1. Registrere og vise aktiviteter")
    print("2. Søke etter eller filtrere kategori")
    print("3. Filtrere etter status")
    print("4. Sortere etter dato eller varighet")
    print("5. Markere en aktivitet som fullført")
    print("6. Vise antall aktiviteter, samlet estimert tid og antall fullførte")
    print("7. Lagre aktiviteter til fil og lese dem inn igjen")
    print("8. Avslutte programmet")


def Read_menu_choice():
    # Leser og validerer menyvalget
    while True:
        choice = input("Velg et alternativ: ").strip()

        if choice in ("1", "2", "3", "4", "5", "6", "7", "8"):
            return choice

        print("Ugyldig menyvalg. Skriv et tall mellom 1 og 8.")


def Main():
    try:
        open(datafil, "r", encoding="utf-8").close()
    except FileNotFoundError:
        try:
            Create_datafile()
            print(
                f"Datafilen {datafil} fantes ikke. "
                "En ny tom datafil er opprettet."
            )
        except OSError as error:
            print(f"Kunne ikke opprette datafilen: {error}")

    activitys = Read_activity()

    while True:
        Show_menu()
        choice = Read_menu_choice()

        if choice == "1":
            Register_activity(activitys)

        elif choice == "2":
            Filt_categories(activitys)

        elif choice == "3":
            Filt_status(activitys)

        elif choice == "4":
            Sort_activitys(activitys)

        elif choice == "5":
            Mark_completed(activitys)

        elif choice == "6":
            Show_stats(activitys)

        elif choice == "7":
            activitys = Save_and_read_activitys(activitys)

        elif choice == "8":
            print("Avslutter programmet.")
            break


if __name__ == "__main__":
    Main()
