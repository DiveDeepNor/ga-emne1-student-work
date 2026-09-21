import csv
from pathlib import Path

# Oppgave 4

# Leser inn CSV og Txt fil

csv_file = Path(__file__).resolve().parent / "supporthenvendelser.csv"
txt_file = Path(__file__).resolve().parent / "support-rapport.txt"
expected_fields = ["id", "category", "minutes", "is_resolved"]

# Starter med å definere noen funksjoner som jeg kan bruke senere.

def les_supporthenvendelser(filename):
    # Leser CSV-filen rad for rad og returnerer bare gyldige rader
    valid_rows = []

    try:
        with open(filename, "r", encoding="utf-8", newline="") as fil:
            file = csv.DictReader(fil)

            if file.fieldnames != expected_fields:
                print(
                    "Feil i CSV-filen: forventet kolonnene "
                    "id, category, minutes, is_resolved."
                )
                return []

            for rownumber, row in enumerate(file, start=2):
                fault = Validates_rows(row)

                if fault is not None:
                    print(f"Rad {rownumber} er ugyldig: {fault}")
                    continue

                valid_rows.append(row)

    except FileNotFoundError:
        print(f"Fant ikke CSV-filen: {filename.name}")
        return []
    except UnicodeDecodeError:
        print("Kunne ikke lese CSV-filen som UTF-8.")
        return []
    except csv.Error as feil:
        print(f"Feil ved lesing av CSV-filen: {feil}")
        return []
    except OSError as feil:
        print(f"Kunne ikke åpne eller lese CSV-filen: {feil}")
        return []

    return valid_rows


def Validates_rows(row):
    # Kontrollerer at feltene er utfylt og har gyldig verdi
    if None in row:
        return "for mange felt i raden"

    for fields in expected_fields:
        value = row.get(fields)
        if value is None or value.strip() == "":
            return f"feltet '{fields}' mangler verdi"

    try:
        id_value = int(row["id"])
    except ValueError:
        return "id må være et heltall"

    if id_value <= 0:
        return "id må være et positivt heltall"

    try:
        minutes = int(row["minutes"])
    except ValueError:
        return "minutes må være et heltall"

    if minutes < 0:
        return "minutes må være 0 eller større"

    if row["is_resolved"] not in ("yes", "no"):
        return "is_resolved må være nøyaktig 'yes' eller 'no'"

    return None


def Sum_resolved_minutes(requests: list[dict[str, str]]) -> int:
    # Returnerer samlet tidsbruk for alle løste henvendelser
    total = 0

    for request in requests:
        if request["is_resolved"] == "yes":
            total += int(request["minutes"])

    return total


def Analyse_data(requests):
    # Beregner statistikk på de gyldige CSV-radene
    count_pr_category = {}
    minutes_pr_category = {}
    number_resolved = 0
    number_unresolved = 0

    for request in requests:
        categori = request["category"]
        minutes = int(request["minutes"])

        if categori not in count_pr_category:
            count_pr_category[categori] = 0
            minutes_pr_category[categori] = 0

        count_pr_category[categori] += 1
        minutes_pr_category[categori] += minutes

        if request["is_resolved"] == "yes":
            number_resolved += 1
        else:
            number_unresolved += 1

    category_stats = {}
    for categori in count_pr_category:
        count = count_pr_category[categori]
        total_time = minutes_pr_category[categori]
        category_stats[categori] = {
            "antall": count,
            "samlet_tid": total_time,
            "gjennomsnitt": total_time / count,
        }

    most_inquiries = []
    if category_stats:
        max_number = max(
            statistikk["antall"]
            for statistikk in category_stats.values()
        )
        most_inquiries = [
            kategori
            for kategori, statistikk in category_stats.items()
            if statistikk["antall"] == max_number
        ]

    unresolved = [
        request
        for request in requests
        if request["is_resolved"] == "no"
    ]
    unresolved_sorted = sorted(
        unresolved,
        key=lambda request: int(request["minutes"]),
        reverse=True,
    )

    return {
        "antall_gyldige": len(requests),
        "antall_per_kategori": count_pr_category,
        "kategori_statistikk": category_stats,
        "antall_loste": number_resolved,
        "antall_uloste": number_unresolved,
        "flest_henvendelser": most_inquiries,
        "uloste_sortert": unresolved_sorted,
        "sum_loste_minutter": Sum_resolved_minutes(requests),
    }


def Report(report_fil, stats):
    # Lager en analysen til rapportfilen og overskriver eventuell gammel fil
    try:
        with open(report_fil, "w", encoding="utf-8") as fil:
            fil.write("SUPPORT-RAPPORT\n")
            fil.write("===============\n\n")

            fil.write(
                f"Antall gyldige henvendelser: {stats['antall_gyldige']}\n"
            )
            fil.write(
                f"Antall løste henvendelser: {stats['antall_loste']}\n"
            )
            fil.write(
                f"Antall uløste henvendelser: {stats['antall_uloste']}\n\n"
            )

            fil.write("Antall henvendelser per kategori:\n")
            for category in sorted(stats["antall_per_kategori"]):
                number = stats["antall_per_kategori"][category]
                fil.write(f"  {category}: {number}\n")

            fil.write("\nTidsbruk per kategori:\n")
            for category in sorted(stats["kategori_statistikk"]):
                data = stats["kategori_statistikk"][category]
                fil.write(f"  {category}:\n")
                fil.write(f"    Samlet tidsbruk: {data['samlet_tid']} minutter\n")
                fil.write(
                    f"    Gjennomsnittlig tidsbruk: {data['gjennomsnitt']:.2f} minutter\n"
                )

            fil.write("\nSamlet tidsbruk for løste henvendelser: ")
            fil.write(f"{stats['sum_loste_minutter']} minutter\n")

            category = stats["flest_henvendelser"]
            if len(category) == 1:
                category = category[0]
                number = stats["antall_per_kategori"][category]
                fil.write(
                    f"\nKategori med flest henvendelser: {category} ({number})\n"
                )
            elif category:
                detaljer = ", ".join(
                    f"{kategori} ({stats['antall_per_kategori'][kategori]})"
                    for kategori in category
                )
                fil.write(f"\nKategorier med flest henvendelser: {detaljer}\n")

            fil.write("\nUløste henvendelser, mest tidkrevende først:\n")
            for request in stats["uloste_sortert"]:
                fil.write(
                    f"  ID {request['id']}: {request['category']} - "
                    f"{request['minutes']} minutter\n"
                )

    except OSError as feil:
        print(f"Kunne ikke skrive rapportfilen: {feil}")
        return False

    return True


def Print_result(stats):
    # Printer analysen i terminalen
    print("\n--- ANALYSE ---")
    print(f"Antall gyldige henvendelser: {stats['antall_gyldige']}")
    print(f"Antall løste henvendelser: {stats['antall_loste']}")
    print(f"Antall uløste henvendelser: {stats['antall_uloste']}")

    print("\nAntall per kategori:")
    for category in sorted(stats["antall_per_kategori"]):
        print(f"{category}: {stats['antall_per_kategori'][category]}")

    print("\nTidsbruk per kategori:")
    for category in sorted(stats["kategori_statistikk"]):
        data = stats["kategori_statistikk"][category]
        print(
            f"{category}: {data['samlet_tid']} minutter totalt, "
            f"gjennomsnitt {data['gjennomsnitt']:.2f} minutter"
        )

    print(
        "\nSamlet tidsbruk for løste henvendelser: "
        f"{stats['sum_loste_minutter']} minutter"
    )

    categorise = stats["flest_henvendelser"]
    if len(categorise) == 1:
        category = categorise[0]
        number = stats["antall_per_kategori"][category]
        print(f"Kategori med flest henvendelser: {category} ({number})")
    elif categorise:
        details = ", ".join(
            f"{category} ({stats['antall_per_kategori'][category]})"
            for category in categorise
        )
        print(f"Kategorier med flest henvendelser: {details}")

    print("\nUløste henvendelser, mest tidkrevende først:")
    for request in stats["uloste_sortert"]:
        print(
            f"ID {request['id']}: {request['category']} - "
            f"{request['minutes']} minutter"
        )


# Hovedprogram

print("--- OPPGAVE 4 – SUPPORTHENVENDELSER ---")

valid_rows = les_supporthenvendelser(csv_file)

if not valid_rows:
    print("Ingen gyldige rader ble funnet. Programmet avsluttes.")
else:
    statistic = Analyse_data(valid_rows)
    Print_result(statistic)

    if Report(txt_file, statistic):
        print(f"\nRapport skrevet til: {txt_file.name}")
