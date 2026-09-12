def read_number():
    return int(input(f"Skriv inn nummer: "))

def describe_sign(number):
    if number > 0:
        return "Postive"
    elif number < 0:
        return "Negative"
    else: return "Zero"

def is_even(number):
    return number % 2 == 0

def show_analysis(number, sign, even):
    print(number, sign, even)

def run_number_analysis():
    number = read_number()
    sign = describe_sign(number)
    even = is_even(number)
    show_analysis(number, sign, even)

run_number_analysis()




