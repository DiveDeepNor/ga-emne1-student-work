secret_pin = 2468
attemps_left = 3
is_authenticated = False

while attemps_left > 0:
    print(f"Forsøk igjen {attemps_left}")
    pin = int(input("Pin kode? "))
    if pin != secret_pin:
        print("Feil pin")
        attemps_left = attemps_left - 1
        if attemps_left == 0:
            print("Access denied")
    else:
        print("Riktig pin")
        attemps_left = 0

