#distance
#fuel_per_100_km
#fuel_price

#kladd for å huske
    #total_cost = int(input("Hva er total kostnad? "))
    #print(f"Ferdig_Pris: {Ferdig_Pris:.2f}")

distance = float(input ("Distanse kjørt? "))
fuel_per_100_km = float (input ("Drivstoff pr. 100 km? "))
fuel_price = float (input ("Drivstoff pris? "))

fuel_quantity = (distance/100.0)*fuel_per_100_km
cost = fuel_quantity * fuel_price
print(f"Drivstoffmengde brukt: {fuel_quantity:.2f}")
print(f"Drivstoffmengde brukt: {cost:.2f}")