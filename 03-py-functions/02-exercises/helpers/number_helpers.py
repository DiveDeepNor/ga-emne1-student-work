def is_even(number):
    """Checks if the number is even or odd. Return a bool value"""
    return number % 2 == 0

def find_largest(first_number, second_number):
    """Finding the larges number, based on the 2 input number. Returns the largest number.
    If equal numbers, the returned value is 0"""
    if first_number > second_number:
        return first_number
    elif first_number < second_number:
        return second_number
    else: return 0