def calculate_area(width, height):
    area = width * height
    return area

total_area = 0
for width in range (2, 5):
    area = calculate_area(width, 2)
    print(f"The total area: {area:.2f} m^2")
    total_area += area

print(f"Total area is: {total_area} m^2")
