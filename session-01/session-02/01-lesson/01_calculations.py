"number_of_tickets = int(input(How, many tickets? ))"
"ticket_price = 180"
"service_fee = 35"

"subtotal = ticket_price * number_of_tickets"
"total = subtotal + service_fee"
"price_per_person = total // number_of_tickets"

"print(total)"
"print(price_per_person)"

total_cost = int(input("Hva er total kostnad? "))
total_persons = int(input("antall personer"))


subtotal = total_cost // total_persons


print(subtotal)


