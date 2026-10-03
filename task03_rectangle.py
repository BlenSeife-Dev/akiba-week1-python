# Task 03 - Rectangle Workshop

# 1. Collect input from the user (converting str to float)
length = float(input("Length: "))
width = float(input("Width: "))

# 2. Perform calculations
area = length * width
perimeter = 2 * (length + width)

# 3. Display results
print(f"Area: {area:.2f} m²")
print(f"Perimeter: {perimeter:.2f} m")