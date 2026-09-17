# Oppgave 1.3

def oppgave_1_3():
    while True:
        while True:
            try:
                start_value= int(input("Skriv inn startverdi: "))
                break

            except ValueError:
                print("Feil: Du må skrive inn et heltall.")

        while True:
            try:
                end_value= int(input("Skriv inn sluttverdi: "))
                break

            except ValueError:
                print("Feil: Du må skrive inn et heltall.")

        if start_value > end_value:
            print("Sluttverdien må være større enn eller lik startverdien.")
        else:
            break


    print(start_value)
    print(end_value)


    # Lager først for partall, så for del på 3 så sum for å få luft mellom tallrangene.

    # partall
    for i in range(start_value, end_value + 1):
        if i % 2 == 0:
            print(i)

    print("\n---\n")
    # del på 3 tall
    for i in range(start_value, end_value + 1):
        if i % 3 == 0:
            print(i)

    print("\n---\n")
    # sum
    total = 0
    for i in range(start_value, end_value + 1):
        total = total + i
    print(total)