UpperLimit = int(input("Hva er den øver grensen? "))
teller = 1

while teller * teller < UpperLimit:
    print(teller*teller)
    teller += 1