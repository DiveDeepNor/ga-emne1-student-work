secret_number = 10
attempts_left = 5
quessed_correctly = False

while attempts_left > 0 and not quessed_correctly:
    guess_nr = int(input("hvilke nummer gjetter du? "))
    if guess_nr == secret_number:
        print("korrekt!")
        quessed_correctly = True

    elif guess_nr > secret_number:
        attempts_left -= 1
        print("for høyt!")

    else:
        attempts_left -= 1
        print("for lavt!")




