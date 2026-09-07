#kladd for å huske
    #total_cost = int(input("Hva er total kostnad? "))
    #print(f"Ferdig_Pris: {Ferdig_Pris:.2f}")
    #float_div = first_number / secound_number
    #int_div = first_number // secound_number
    #rest_div = float_div % int_div
    #if score >= 90:
        #print("Good!")
    #elif score >= 60:
        #print("Tja!")
    #else:
        #print("Dårlig!)")


pakkevekt = float(input("Hva veier pakken i kg? "))
frakt = 0

if pakkevekt <= 0.0:
    print("Pakken kan ikke veien 0 eller mindre")

elif pakkevekt <= 2.0 :
    frakt = 79

elif pakkevekt <= 5.0:
    frakt = 129

elif pakkevekt <= 10.0:
    frakt = 199

elif pakkevekt > 10.0:
    print("Pakken kan er for tung for å sendes")

if frakt != 0:
    print(f"Fraktkostnad: {frakt}")
else:
    print("Pakken kan ikke sendes")