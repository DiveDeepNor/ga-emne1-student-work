def find_largest(first_number, second_number):
    if first_number > second_number:
        return first_number
    elif first_number < second_number:
        return second_number
    else: return 0

number = find_largest(10, 20)
print (number)

print(find_largest(22, 2))
print(find_largest(15,15))