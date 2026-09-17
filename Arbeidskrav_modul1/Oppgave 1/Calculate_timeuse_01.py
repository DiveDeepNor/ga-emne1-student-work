# Oppgave 1.1
    #Leser først inn studieøkter, og sjekker at input er en gyldig verdi
def oppgave_1_1():
    while True:
        try:
            antall_okter = int(input("Hvor mange studieøkter? "))

            if antall_okter <= 0:
                print("Feil: Skriv inn et positivt heltall.")
            else:
                break

        except ValueError:
            print("Feil: Du må skrive inn et heltall.")

        #Leser så inn minutter pr økt, og sjekker at input er en gyldig verdi
    while True:
        try:
            minutter_per_okt = int(input("Hvor mange minutter per økt? "))

            if minutter_per_okt <= 0:
                print("Feil: Skriv inn et positivt heltall.")
            else:
                break

        except ValueError:
            print("Feil: Du må skrive inn et heltall.")

        #Regne sammen og deler opp i timer og minutter
    samlet_tidsbruk = int((antall_okter * minutter_per_okt))
    samlet_tidsbruk_timer = samlet_tidsbruk // 60
    samlet_tidsbruk_minutter = samlet_tidsbruk % 60

    print(print (f" Samlet tidsbruk:  {samlet_tidsbruk_timer} timer og {samlet_tidsbruk_minutter} minutter"))


