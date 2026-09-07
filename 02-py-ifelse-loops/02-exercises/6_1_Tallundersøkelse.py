i = 1

while i <= 20:
    rest = i % 2
    if rest == 0:
        print(f"{i}, tallet er er et partall")
    else:
        print(f"{i}, tallet er er et oddetall")
    i += 1
