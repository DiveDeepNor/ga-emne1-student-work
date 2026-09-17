def registrer_studieokt(studieokter):

    print("\n---\n")
    topic = input("Hva skal du studere? ")
    while True:
        try:
            duration_minutes = int(input("Hvor lenge skal du studere? "))
            if duration_minutes > 0:
                break
            else:
                print("Ugyldig verdi!")
        except ValueError:
                print("Ugyldig verdi!")
    while True:
            status = input("Status (planned/completed): ")

            if status == "planned" or status == "completed":
                break
            else:
                print("Ugyldig status!")

    studieokter.append({
        "topic": topic,
        "duration_minutes": duration_minutes,
        "status": status
    })


def vis_alle_studieokter(studieokter):
    for studieokt in studieokter:
        print("\n---\n")
        print(f"Tema: {studieokt['topic']}")
        print(f"Varighet: {studieokt['duration_minutes']}")
        print(f"Status: {studieokt['status']}")

def vis_fullforte_studieokter(studieokter):
    for studieokt in studieokter:
        if studieokt["status"] == "completed":
            print("\n---\n")
            print(f"Tema: {studieokt['topic']}")
            print(f"Varighet: {studieokt['duration_minutes']}")
            print(f"Status: {studieokt['status']}")

def sok_i_tema(studieokter):
    sokeord = input("Hva vil du søke etter? ")
    for studieokt in studieokter:
        if sokeord.lower() in studieokt["topic"].lower():
            print("\n---\n")
            print(f"Tema: {studieokt['topic']}")
            print(f"Varighet: {studieokt['duration_minutes']}")
            print(f"Status: {studieokt['status']}")

def sorter_etter_varighet(studieokter):
    sorterte_okter = sorted(
        studieokter,
        key=lambda studieokt: studieokt["duration_minutes"],
        reverse=True
    )

    for studieokt in sorterte_okter:
        print("\n---\n")
        print(f"Tema: {studieokt['topic']}")
        print(f"Varighet: {studieokt['duration_minutes']}")
        print(f"Status: {studieokt['status']}")


def vis_varighet_statistikk(studieokter):
    fullforte = []

    for studieokt in studieokter:
        if studieokt["status"] == "completed":
            fullforte.append(studieokt)

    if len(fullforte) == 0:
        print("Ingen fullførte studieøkter.")
        return

    total_varighet = 0

    for studieokt in fullforte:
        total_varighet = total_varighet + studieokt["duration_minutes"]

    gjennomsnitt = total_varighet / len(fullforte)

    print(f"Samlet varighet: {total_varighet} minutter")
    print(f"Gjennomsnittlig varighet: {gjennomsnitt:.1f} minutter")


studieokter = []

studieokter.append({
    "topic": "Python",
    "duration_minutes": 60,
    "status": "completed"
})

studieokter.append({
    "topic": "C++",
    "duration_minutes": 120,
    "status": "planned"
})

studieokter.append({
    "topic": "SQL",
    "duration_minutes": 180,
    "status": "completed"
})

studieokter.append({
    "topic": "JAVA",
    "duration_minutes": 240,
    "status": "planned"
})

studieokter.append({
    "topic": "HTML",
    "duration_minutes": 300,
    "status": "completed"
})

while True:
    print("\n--- MENY ---")
    print("1. Registrer studieøkt")
    print("2. Vis alle studieøkter")
    print("3. Vis fullførte studieøkter")
    print("4. Søk etter ord i tema")
    print("5. Sorter etter varighet, lengst først")
    print("6. Vis samlet og gjennomsnittlig varighet")
    print("7. Avslutt")
    while True:
        # Leser inn valg
        try:
            meny_valg = int(input("Velg: "))

            if meny_valg > 7 or meny_valg < 1:
                print("Error: Du må skrive inn et tall mellom 1 og 7")
            else:
                break
        except ValueError:
            print("Error: Du må skrive inn et tall mellom 1 og 7")

    if meny_valg == 1:
        registrer_studieokt(studieokter)
    elif meny_valg == 2:
        vis_alle_studieokter(studieokter)
    elif meny_valg == 3:
        vis_fullforte_studieokter(studieokter)
    elif meny_valg == 4:
        sok_i_tema(studieokter)
    elif meny_valg == 5:
        sorter_etter_varighet(studieokter)
    elif meny_valg == 6:
        vis_varighet_statistikk(studieokter)
    elif meny_valg == 7:
        print("Avslutter programmet.")
        break


