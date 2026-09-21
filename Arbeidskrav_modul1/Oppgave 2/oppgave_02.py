# Oppgave 2

# Starter med å definere noen funksjoner som jeg bruker senere.

def Reg_study_session(sessions):

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

    sessions.append({
        "topic": topic,
        "duration_minutes": duration_minutes,
        "status": status
    })


def Show_all_sessions(sessions):
    for session in sessions:
        print("\n---\n")
        print(f"Tema: {session['topic']}")
        print(f"Varighet: {session['duration_minutes']}")
        print(f"Status: {session['status']}")

def Show_completed_sessions(sessions):
    for session in sessions:
        if session["status"] == "completed":
            print("\n---\n")
            print(f"Tema: {session['topic']}")
            print(f"Varighet: {session['duration_minutes']}")
            print(f"Status: {session['status']}")

def Search_subject(sessions):
    keyword = input("Hva vil du søke etter? ")
    for session in sessions:
        if keyword.lower() in session["topic"].lower():
            print("\n---\n")
            print(f"Tema: {session['topic']}")
            print(f"Varighet: {session['duration_minutes']}")
            print(f"Status: {session['status']}")

def Sort_by_duration(sessions):
    sorted_sessions = sorted(
        sessions,
        key=lambda session: session["duration_minutes"],
        reverse=True
    )

    for sessions in sorted_sessions:
        print("\n---\n")
        print(f"Tema: {sessions['topic']}")
        print(f"Varighet: {sessions['duration_minutes']}")
        print(f"Status: {sessions['status']}")


def Show_duration_stats(sessions):
    completed = []

    for session in sessions:
        if session["status"] == "completed":
            completed.append(session)

    if len(completed) == 0:
        print("Ingen fullførte studieøkter.")
        return

    total_duration = 0

    for session in completed:
        total_duration = total_duration + session["duration_minutes"]

    average = total_duration / len(completed)

    print(f"Samlet varighet: {total_duration} minutter")
    print(f"Gjennomsnittlig varighet: {average:.1f} minutter")

# Sessions under er lagt inn for test. Litt ulike topics, duration og status.

sessions = []

sessions.append({
    "topic": "Python",
    "duration_minutes": 60,
    "status": "completed"
})

sessions.append({
    "topic": "C++",
    "duration_minutes": 120,
    "status": "planned"
})

sessions.append({
    "topic": "SQL",
    "duration_minutes": 180,
    "status": "completed"
})

sessions.append({
    "topic": "JAVA",
    "duration_minutes": 240,
    "status": "planned"
})

sessions.append({
    "topic": "HTML",
    "duration_minutes": 300,
    "status": "completed"
})


# Selve programmet.

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
            menu_choice = int(input("Velg: "))

            if menu_choice > 7 or menu_choice < 1:
                print("Error: Du må skrive inn et tall mellom 1 og 7")
            else:
                break
        except ValueError:
            print("Error: Du må skrive inn et tall mellom 1 og 7")

    if menu_choice == 1:
        Reg_study_session(sessions)
    elif menu_choice == 2:
        Show_all_sessions(sessions)
    elif menu_choice == 3:
        Show_completed_sessions(sessions)
    elif menu_choice == 4:
        Search_subject(sessions)
    elif menu_choice == 5:
        Sort_by_duration(sessions)
    elif menu_choice == 6:
        Show_duration_stats(sessions)
    elif menu_choice == 7:
        print("Avslutter programmet.")
        break


