product_name = input('Skriv navnet på produktet ')
unit_price = float(input(f'Hva koster {product_name} pr. stk? '))
Quantity = int(input(f'Hvor mange {product_name} har du?'))

total = unit_price * Quantity

print(f'Pris for alle bollene er: {total:.2f},-')
