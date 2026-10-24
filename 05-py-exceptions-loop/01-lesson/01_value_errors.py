try:
    age = int(input("Age: "))
except ValueError:
    print("Error: Only integers are valid!")
else:
    print(f"Next year: {age +1}")
print("Done")