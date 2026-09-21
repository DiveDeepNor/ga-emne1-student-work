# Oppgave 1.2

def Task_1_2():
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

    text_length = len(text)
    text_length_strip = len(text.replace(" ",""))
    bakwards = text[::-1]


    print(text_length)
    print(text_length_strip)
    print(bakwards)
    if "python" in text.lower():
        print("Python er skrevet")
    else:
        print("Python er ikke skrevet")
