import csv
from pathlib import Path


CSV_FIL = Path(__file__).resolve().parent / "supporthenvendelser.csv"
RAPPORT_FIL = Path(__file__).resolve().parent / "support-rapport.txt"
FORVENTEDE_FELT = ["id", "category", "minutes", "is_resolved"]


def les_supporthenvendelser(filnavn):
    """Leser CSV-filen rad for rad og returnerer bare gyldige rader."""
    gyldige_rader = []

    try:
        with open(filnavn, "r", encoding="utf-8", newline="") as fil:
            leser = csv.DictReader(fil)

            if leser.fieldnames != FORVENTEDE_FELT:
                print(
                    "Feil i CSV-filen: forventet kolonnene "
                    "id, category, minutes, is_resolved."
                )
                return []

            for radnummer, rad in enumerate(leser, start=2):
                problem = valider_rad(rad)

                if problem is not None:
                    print(f"Rad {radnummer} er ugyldig: {problem}")
                    continue

                gyldige_rader.append(rad)

    except FileNotFoundError:
        print(f"Fant ikke CSV-filen: {filnavn.name}")
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

    return gyldige_rader


def valider_rad(rad):
    """Kontrollerer at alle feltene er utfylt og har gyldig verdi."""
    if None in rad:
        return "for mange felt i raden"

    for felt in FORVENTEDE_FELT:
        verdi = rad.get(felt)
        if verdi is None or verdi.strip() == "":
            return f"feltet '{felt}' mangler verdi"

    try:
        id_verdi = int(rad["id"])
    except ValueError:
        return "id må være et heltall"

    if id_verdi <= 0:
        return "id må være et positivt heltall"

    try:
        minutter = int(rad["minutes"])
    except ValueError:
        return "minutes må være et heltall"

    if minutter < 0:
        return "minutes må være 0 eller større"

    if rad["is_resolved"] not in ("yes", "no"):
        return "is_resolved må være nøyaktig 'yes' eller 'no'"

    return None


def sum_resolved_minutes(requests: list[dict[str, str]]) -> int:
    """Returnerer samlet tidsbruk for alle løste henvendelser."""
    total = 0

    for request in requests:
        if request["is_resolved"] == "yes":
            total += int(request["minutes"])

    return total


def analyser_data(requests):
    """Beregner statistikk basert på de gyldige CSV-radene."""
    antall_per_kategori = {}
    minutter_per_kategori = {}
    antall_loste = 0
    antall_uloste = 0

    for request in requests:
        kategori = request["category"]
        minutter = int(request["minutes"])

        if kategori not in antall_per_kategori:
            antall_per_kategori[kategori] = 0
            minutter_per_kategori[kategori] = 0

        antall_per_kategori[kategori] += 1
        minutter_per_kategori[kategori] += minutter

        if request["is_resolved"] == "yes":
            antall_loste += 1
        else:
            antall_uloste += 1

    kategori_statistikk = {}
    for kategori in antall_per_kategori:
        antall = antall_per_kategori[kategori]
        samlet_tid = minutter_per_kategori[kategori]
        kategori_statistikk[kategori] = {
            "antall": antall,
            "samlet_tid": samlet_tid,
            "gjennomsnitt": samlet_tid / antall,
        }

    flest_henvendelser = []
    if kategori_statistikk:
        maks_antall = max(
            statistikk["antall"]
            for statistikk in kategori_statistikk.values()
        )
        flest_henvendelser = [
            kategori
            for kategori, statistikk in kategori_statistikk.items()
            if statistikk["antall"] == maks_antall
        ]

    uloste = [
        request
        for request in requests
        if request["is_resolved"] == "no"
    ]
    uloste_sortert = sorted(
        uloste,
        key=lambda request: int(request["minutes"]),
        reverse=True,
    )

    return {
        "antall_gyldige": len(requests),
        "antall_per_kategori": antall_per_kategori,
        "kategori_statistikk": kategori_statistikk,
        "antall_loste": antall_loste,
        "antall_uloste": antall_uloste,
        "flest_henvendelser": flest_henvendelser,
        "uloste_sortert": uloste_sortert,
        "sum_loste_minutter": sum_resolved_minutes(requests),
    }


def skriv_rapport(rapport_fil, statistikk):
    """Skriver analysen til rapportfilen og overskriver eventuell gammel rapport."""
    try:
        with open(rapport_fil, "w", encoding="utf-8") as fil:
            fil.write("SUPPORT-RAPPORT\n")
            fil.write("===============\n\n")

            fil.write(
                f"Antall gyldige henvendelser: {statistikk['antall_gyldige']}\n"
            )
            fil.write(
                f"Antall løste henvendelser: {statistikk['antall_loste']}\n"
            )
            fil.write(
                f"Antall uløste henvendelser: {statistikk['antall_uloste']}\n\n"
            )

            fil.write("Antall henvendelser per kategori:\n")
            for kategori in sorted(statistikk["antall_per_kategori"]):
                antall = statistikk["antall_per_kategori"][kategori]
                fil.write(f"  {kategori}: {antall}\n")

            fil.write("\nTidsbruk per kategori:\n")
            for kategori in sorted(statistikk["kategori_statistikk"]):
                data = statistikk["kategori_statistikk"][kategori]
                fil.write(f"  {kategori}:\n")
                fil.write(f"    Samlet tidsbruk: {data['samlet_tid']} minutter\n")
                fil.write(
                    f"    Gjennomsnittlig tidsbruk: {data['gjennomsnitt']:.2f} minutter\n"
                )

            fil.write("\nSamlet tidsbruk for løste henvendelser: ")
            fil.write(f"{statistikk['sum_loste_minutter']} minutter\n")

            kategorier = statistikk["flest_henvendelser"]
            if len(kategorier) == 1:
                kategori = kategorier[0]
                antall = statistikk["antall_per_kategori"][kategori]
                fil.write(
                    f"\nKategori med flest henvendelser: {kategori} ({antall})\n"
                )
            elif kategorier:
                detaljer = ", ".join(
                    f"{kategori} ({statistikk['antall_per_kategori'][kategori]})"
                    for kategori in kategorier
                )
                fil.write(f"\nKategorier med flest henvendelser: {detaljer}\n")

            fil.write("\nUløste henvendelser, mest tidkrevende først:\n")
            for request in statistikk["uloste_sortert"]:
                fil.write(
                    f"  ID {request['id']}: {request['category']} - "
                    f"{request['minutes']} minutter\n"
                )

    except OSError as feil:
        print(f"Kunne ikke skrive rapportfilen: {feil}")
        return False

    return True


def skriv_terminalresultat(statistikk):
    """Viser analysen i terminalen."""
    print("\n--- ANALYSE ---")
    print(f"Antall gyldige henvendelser: {statistikk['antall_gyldige']}")
    print(f"Antall løste henvendelser: {statistikk['antall_loste']}")
    print(f"Antall uløste henvendelser: {statistikk['antall_uloste']}")

    print("\nAntall per kategori:")
    for kategori in sorted(statistikk["antall_per_kategori"]):
        print(f"{kategori}: {statistikk['antall_per_kategori'][kategori]}")

    print("\nTidsbruk per kategori:")
    for kategori in sorted(statistikk["kategori_statistikk"]):
        data = statistikk["kategori_statistikk"][kategori]
        print(
            f"{kategori}: {data['samlet_tid']} minutter totalt, "
            f"gjennomsnitt {data['gjennomsnitt']:.2f} minutter"
        )

    print(
        "\nSamlet tidsbruk for løste henvendelser: "
        f"{statistikk['sum_loste_minutter']} minutter"
    )

    kategorier = statistikk["flest_henvendelser"]
    if len(kategorier) == 1:
        kategori = kategorier[0]
        antall = statistikk["antall_per_kategori"][kategori]
        print(f"Kategori med flest henvendelser: {kategori} ({antall})")
    elif kategorier:
        detaljer = ", ".join(
            f"{kategori} ({statistikk['antall_per_kategori'][kategori]})"
            for kategori in kategorier
        )
        print(f"Kategorier med flest henvendelser: {detaljer}")

    print("\nUløste henvendelser, mest tidkrevende først:")
    for request in statistikk["uloste_sortert"]:
        print(
            f"ID {request['id']}: {request['category']} - "
            f"{request['minutes']} minutter"
        )


# Hovedprogram

print("--- OPPGAVE 4 – SUPPORTHENVENDELSER ---")

gyldige_rader = les_supporthenvendelser(CSV_FIL)

if not gyldige_rader:
    print("Ingen gyldige rader ble funnet. Programmet avsluttes.")
else:
    statistikk = analyser_data(gyldige_rader)
    skriv_terminalresultat(statistikk)

    if skriv_rapport(RAPPORT_FIL, statistikk):
        print(f"\nRapport skrevet til: {RAPPORT_FIL.name}")
