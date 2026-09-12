from helpers.number_helpers import *

number = find_largest(10, 20)
print (number)

print(find_largest(22, 2))
print(find_largest(15,15))



def read_number():
    return int(input(f"Skriv inn nummer: "))

def describe_sign(number):
    if number > 0:
        return "Postive"
    elif number < 0:
        return "Negative"
    else: return "Zero"

def show_analysis(number, sign, even):
    print(number, sign, even)

def run_number_analysis():
    number = read_number()
    sign = describe_sign(number)
    even = is_even(number)
    show_analysis(number, sign, even)

run_number_analysis()