number = int(input("Hva er tallet? "))

if number > 0:
    print(f"{number}, Tallet er positivt")
elif number < 0:
    print(f"{number}, Tallet er negativt")
else:
     print(f"{number}, Tallet er null")

if number >1 or number <-1:
    rest = (number / 2) % (number // 2)

    if rest == 0:
        print(f"Tallet er et partall")
    else:
        print (f"Tallet er et oddetall")

if number == 0:
    print(f"Tallet er et partall tja?")

if number == 1 or number == -1:
    print(f"Tallet er et partall")