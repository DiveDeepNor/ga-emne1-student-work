# Oppgave 1.2

def oppgave_1_2():
    while True:
        text = input("Skriv inn tekst: ")
        if not text.strip():
            print("Feil: Skriv inn en tekst, ikke bare mellomrom.")
            continue
        try:
            number = float(text)
            print("Feil: Du må skrive inn tekst ikke et tall.")
            continue
        except ValueError:
            break

    antall_full = len(text)
    antall_strip = len(text.replace(" ",""))
    baklengs = text[::-1]


    print(antall_full)
    print(antall_strip)
    print(baklengs)
    if "python" in text.lower():
        print("Python er skrevet")
    else:
        print("Python er ikke skrevet")
