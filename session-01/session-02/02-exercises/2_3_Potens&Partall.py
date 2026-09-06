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


number = int(input("Hva er tallet? "))
number2 = number ** 2
number3 = number ** 3
rest = (number / 2) % (number // 2)

print(f"Tallet opphøyd i andre: {number2}")
print(f"Tallet opphøyd i tredje: {number3}")
print(f"Tallets rest er: {rest:.1f}")

if rest == 0:
    print(f"Tallet er et partall")
else:
    print (f"Tallet er et oddetall")





