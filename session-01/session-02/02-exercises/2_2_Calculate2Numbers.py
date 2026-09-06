#kladd for å huske
    #total_cost = int(input("Hva er total kostnad? "))
    #print(f"Ferdig_Pris: {Ferdig_Pris:.2f}")

first_number = int(input("Hva er første tall? "))
secound_number = int(input("Hva er andre tall? "))

sum_numbers = first_number + secound_number
diff_numbers = first_number - secound_number
product_numbers = first_number * secound_number
float_div = first_number / secound_number
int_div = first_number // secound_number
rest_div = float_div % int_div

print(f"Sum nummer: {sum_numbers}")
print(f"Differanse nummer: {diff_numbers}")
print(f"Produkt nummer: {product_numbers}")
print(f"Flyttall divisjon: {float_div:.2f}")
print(f"Heltall divisjon: {int_div}")
print(f"Rest divisjon: {rest_div:.2f}")