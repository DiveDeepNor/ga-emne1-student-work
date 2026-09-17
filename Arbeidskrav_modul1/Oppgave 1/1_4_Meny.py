from Calculate_timeuse_01 import *
from Analyse_text_02 import *
from Analyse_number_03 import *

while True:
    # Meny
    print("\n---\n")
    print("OPPGAVE MENY")
    print("Valg 1: Oppgave 1: Beregne tidsbruk")
    print("Valg 2: Oppgave 1: Analyser tekst")
    print("Valg 3: Oppgave 3: Analyser tallinvertvall")
    print("Valg 4: Avslutt")
    print("\n---\n")
    while True:
        # Leser inn valg
        try:
            meny_valg = int(input("Skriv inn menyvalg: "))
            break

        except ValueError:
            print("Feil: Du må skrive inn et tall mellom 1 og 4.")

    if meny_valg > 4 or meny_valg < 1:
        print("Valg må være mellom 1 og 4")
    elif meny_valg == 1:
            oppgave_1_1()
    elif meny_valg == 2:
            oppgave_1_2()
    elif meny_valg == 3:
            oppgave_1_3()
    elif meny_valg == 4:
            print("Velkommen igjen!")
            break


