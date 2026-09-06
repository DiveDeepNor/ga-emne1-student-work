number1 = int(input("Hva er det første tallet? "))
number2 = int(input("Hva er det andre tallet? "))

if number1 > number2:
    print("Det første tallet er størst")
elif number1 < number2:
    print("Det andre tallet er størst")
else:
    print("Tallene er like")