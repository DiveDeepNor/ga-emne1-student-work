import csv
from datetime import datetime


DATAFIL = "aktiviteter.csv"
DATOFORMAT = "%d.%m.%Y"


class Aktivitet:
    """Representerer én aktivitet i aktivitetsplanleggeren."""

    def __init__(self, title, category, date, estimated_minutes, status="planned"):
        self.title = title
        self.category = category
        self.date = date
        self.estimated_minutes = estimated_minutes
        self.status = status

    def mark_completed(self):
        """Markerer aktiviteten som fullført."""
        self.status = "completed"


def les_tekst(prompt):
    """Leser inn tekst og kontrollerer at feltet ikke er tomt."""
    while True:
        tekst = input(prompt).strip()

        if tekst:
            return tekst

        print("Feltet kan ikke være tomt. Prøv igjen.")


def les_dato(prompt):
    """Leser inn en dato på formatet dd.mm.åååå."""
    while True:
        dato_tekst = input(prompt).strip()

        try:
            return datetime.strptime(dato_tekst, DATOFORMAT)
        except ValueError:
            print("Ugyldig dato. Bruk formatet dd.mm.åååå.")


def les_positivt_heltall(prompt):
    """Leser inn et positivt heltall."""
    while True:
        verdi_tekst = input(prompt).strip()

        try:
            verdi = int(verdi_tekst)

            if verdi > 0:
                return verdi

            print("Verdien må være et positivt heltall.")

        except ValueError:
            print("Du må skrive inn et positivt heltall.")


def les_status(prompt="Status (planned/completed): "):
    """Leser inn en gyldig status."""
    while True:
        status = input(prompt).strip().lower()

        if status in ("planned", "completed"):
            return status

        print("Ugyldig status. Skriv planned eller completed.")


def vis_aktiviteter(aktiviteter):
    """Viser aktiviteter på en oversiktlig måte."""
    if not aktiviteter:
        print("Ingen aktiviteter å vise.")
        return

    for nummer, aktivitet in enumerate(aktiviteter, start=1):
        print(
            f"{nummer}. {aktivitet.title} | "
            f"{aktivitet.category} | "
            f"{aktivitet.date.strftime(DATOFORMAT)} | "
            f"{aktivitet.estimated_minutes} min | "
            f"{aktivitet.status}"
        )


def registrer_aktivitet(aktiviteter):
    """Registrerer en ny aktivitet og viser aktivitetslisten."""
    print("\n--- REGISTRER AKTIVITET ---")

    title = les_tekst("Tittel: ")
    category = les_tekst("Kategori: ")
    date = les_dato("Dato (dd.mm.åååå): ")
    estimated_minutes = les_positivt_heltall("Estimert tid i minutter: ")

    aktivitet = Aktivitet(
        title,
        category,
        date,
        estimated_minutes
    )

    aktiviteter.append(aktivitet)

    print("Aktiviteten er registrert.")
    print("\n--- AKTIVITETER ---")
    vis_aktiviteter(aktiviteter)


def filtrer_kategori(aktiviteter):
    """Søker etter tekst i aktivitetskategorien."""
    if not aktiviteter:
        print("Ingen aktiviteter registrert.")
        return

    soketekst = les_tekst("Skriv inn kategori du vil søke etter: ").lower()

    resultat = [
        aktivitet
        for aktivitet in aktiviteter
        if soketekst in aktivitet.category.lower()
    ]

    if not resultat:
        print("Ingen aktiviteter funnet i denne kategorien.")
        return

    print("\n--- RESULTAT ---")
    vis_aktiviteter(resultat)


def filtrer_status(aktiviteter):
    """Viser aktiviteter med valgt status."""
    if not aktiviteter:
        print("Ingen aktiviteter registrert.")
        return

    status = les_status()

    resultat = [
        aktivitet
        for aktivitet in aktiviteter
        if aktivitet.status == status
    ]

    if not resultat:
        print(f"Ingen aktiviteter med status '{status}'.")
        return

    print("\n--- RESULTAT ---")
    vis_aktiviteter(resultat)


def sorter_aktiviteter(aktiviteter):
    """Sorterer aktiviteter etter dato eller estimert varighet."""
    if not aktiviteter:
        print("Ingen aktiviteter registrert.")
        return

    while True:
        valg = input(
            "Sorter etter 1 = dato (eldste først), "
            "2 = varighet (lengst først): "
        ).strip()

        if valg in ("1", "2"):
            break

        print("Ugyldig valg. Skriv 1 eller 2.")

    if valg == "1":
        sorterte = sorted(aktiviteter, key=lambda aktivitet: aktivitet.date)
    else:
        sorterte = sorted(
            aktiviteter,
            key=lambda aktivitet: aktivitet.estimated_minutes,
            reverse=True
        )

    print("\n--- SORTERTE AKTIVITETER ---")
    vis_aktiviteter(sorterte)


def marker_fullfort(aktiviteter):
    """Lar brukeren markere en planlagt aktivitet som fullført."""
    planlagte = [
        aktivitet
        for aktivitet in aktiviteter
        if aktivitet.status == "planned"
    ]

    if not planlagte:
        print("Ingen planlagte aktiviteter å markere som fullført.")
        return

    print("\n--- PLANLAGTE AKTIVITETER ---")
    vis_aktiviteter(planlagte)

    while True:
        valg = input("Velg nummeret på aktiviteten som skal fullføres: ").strip()

        try:
            nummer = int(valg)

            if 1 <= nummer <= len(planlagte):
                planlagte[nummer - 1].mark_completed()
                print("Aktiviteten er markert som fullført.")
                return

            print("Nummeret finnes ikke. Prøv igjen.")

        except ValueError:
            print("Du må skrive inn et helt tall.")


def vis_statistikk(aktiviteter):
    """Viser antall aktiviteter, samlet estimert tid og antall fullførte."""
    antall_aktiviteter = len(aktiviteter)

    samlet_tid = sum(
        aktivitet.estimated_minutes
        for aktivitet in aktiviteter
    )

    antall_fullforte = sum(
        1
        for aktivitet in aktiviteter
        if aktivitet.status == "completed"
    )

    print("\n--- STATISTIKK ---")
    print(f"Antall aktiviteter: {antall_aktiviteter}")
    print(f"Samlet estimert tid: {samlet_tid} minutter")
    print(f"Antall fullførte: {antall_fullforte}")


def opprett_datafil():
    """Oppretter en tom CSV-fil med riktig overskriftsrad."""
    with open(DATAFIL, "w", newline="", encoding="utf-8") as fil:
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


def aktivitet_til_rad(aktivitet):
    """Gjør en Aktivitet om til en dictionary for CSV."""
    return {
        "title": aktivitet.title,
        "category": aktivitet.category,
        "date": aktivitet.date.strftime(DATOFORMAT),
        "estimated_minutes": str(aktivitet.estimated_minutes),
        "status": aktivitet.status
    }


def rad_til_aktivitet(rad):
    """Gjør en CSV-rad om til en Aktivitet."""
    title = (rad.get("title") or "").strip()
    category = (rad.get("category") or "").strip()
    date_tekst = (rad.get("date") or "").strip()
    minutes_tekst = (rad.get("estimated_minutes") or "").strip()
    status = (rad.get("status") or "").strip().lower()

    if not title:
        raise ValueError("tittel mangler")

    if not category:
        raise ValueError("kategori mangler")

    try:
        date = datetime.strptime(date_tekst, DATOFORMAT)
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

    return Aktivitet(
        title,
        category,
        date,
        estimated_minutes,
        status
    )


def lagre_aktiviteter(aktiviteter):
    """Lagrer alle aktiviteter til CSV-filen."""
    try:
        with open(DATAFIL, "w", newline="", encoding="utf-8") as fil:
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

            for aktivitet in aktiviteter:
                writer.writerow(aktivitet_til_rad(aktivitet))

        return True

    except OSError as error:
        print(f"Kunne ikke lagre datafilen: {error}")
        return False


def les_aktiviteter():
    """Leser aktiviteter fra CSV-filen."""
    try:
        with open(DATAFIL, "r", newline="", encoding="utf-8") as fil:
            reader = csv.DictReader(fil)

            forventede_felter = {
                "title",
                "category",
                "date",
                "estimated_minutes",
                "status"
            }

            if reader.fieldnames is None or not forventede_felter.issubset(
                set(reader.fieldnames)
            ):
                print("Datafilen har feil format. Starter med en tom samling.")
                return []

            aktiviteter = []

            for rad_nr, rad in enumerate(reader, start=2):
                try:
                    aktivitet = rad_til_aktivitet(rad)
                    aktiviteter.append(aktivitet)
                except ValueError as error:
                    print(f"Rad {rad_nr} ble hoppet over: {error}.")

            return aktiviteter

    except (OSError, csv.Error) as error:
        print(f"Kunne ikke lese datafilen: {error}")
        print("Programmet fortsetter med en tom samling.")
        return []


def lagre_og_les_aktiviteter(aktiviteter):
    """Lagrer aktivitetene og leser dem inn igjen."""
    if not lagre_aktiviteter(aktiviteter):
        return aktiviteter

    print("Aktivitetene er lagret til datafilen.")

    innlastede_aktiviteter = les_aktiviteter()
    print("Aktivitetene er lest inn igjen fra datafilen.")

    return innlastede_aktiviteter


def vis_meny():
    """Viser hovedmenyen."""
    print("\n--- MENY ---")
    print("1. Registrere og vise aktiviteter")
    print("2. Søke etter eller filtrere kategori")
    print("3. Filtrere etter status")
    print("4. Sortere etter dato eller varighet")
    print("5. Markere en aktivitet som fullført")
    print("6. Vise antall aktiviteter, samlet estimert tid og antall fullførte")
    print("7. Lagre aktiviteter til fil og lese dem inn igjen")
    print("8. Avslutte programmet")


def les_menyvalg():
    """Leser og validerer menyvalget."""
    while True:
        valg = input("Velg et alternativ: ").strip()

        if valg in ("1", "2", "3", "4", "5", "6", "7", "8"):
            return valg

        print("Ugyldig menyvalg. Skriv et tall mellom 1 og 8.")


def main():
    try:
        open(DATAFIL, "r", encoding="utf-8").close()
    except FileNotFoundError:
        try:
            opprett_datafil()
            print(
                f"Datafilen {DATAFIL} fantes ikke. "
                "En ny tom datafil er opprettet."
            )
        except OSError as error:
            print(f"Kunne ikke opprette datafilen: {error}")

    aktiviteter = les_aktiviteter()

    while True:
        vis_meny()
        valg = les_menyvalg()

        if valg == "1":
            registrer_aktivitet(aktiviteter)

        elif valg == "2":
            filtrer_kategori(aktiviteter)

        elif valg == "3":
            filtrer_status(aktiviteter)

        elif valg == "4":
            sorter_aktiviteter(aktiviteter)

        elif valg == "5":
            marker_fullfort(aktiviteter)

        elif valg == "6":
            vis_statistikk(aktiviteter)

        elif valg == "7":
            aktiviteter = lagre_og_les_aktiviteter(aktiviteter)

        elif valg == "8":
            print("Avslutter programmet.")
            break


if __name__ == "__main__":
    main()
