# Oppgave 1.1
    #Leser først inn studieøkter, og sjekker at input er en gyldig verdi
def Task_1_1():
    while True:
        try:
            sessions_nr = int(input("Hvor mange studieøkter? "))

            if sessions_nr <= 0:
                print("Feil: Skriv inn et positivt heltall.")
            else:
                break

        except ValueError:
            print("Feil: Du må skrive inn et heltall.")

        #Leser så inn minutter pr økt, og sjekker at input er en gyldig verdi
    while True:
        try:
            min_pr_session = int(input("Hvor mange minutter per økt? "))

            if min_pr_session <= 0:
                print("Feil: Skriv inn et positivt heltall.")
            else:
                break

        except ValueError:
            print("Feil: Du må skrive inn et heltall.")

        #Regne sammen og deler opp i timer og minutter
    total_time = int((sessions_nr * min_pr_session))
    total_time_hours = total_time // 60
    total_time_minutes = total_time % 60

    print(print (f" Samlet tidsbruk:  {total_time_hours} timer og {total_time_minutes} minutter"))


