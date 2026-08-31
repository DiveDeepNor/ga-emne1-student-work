Pris = float(input("Kjøpt for: "))

if Pris >= 1000:
    Rabatt = 0.2
elif Pris >= 500:
    Rabatt = 0.1
else: Rabatt = 0

Ferdig_Pris = Pris * (1-Rabatt)
print(f"Ferdig_Pris: {Ferdig_Pris:.2f}")


