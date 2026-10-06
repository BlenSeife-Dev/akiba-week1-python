name = input("Name: ")
weight = float(input("Weight in kilograms: "))
height = float(input("Height in meters: "))

bmi = weight / (height ** 2)

print("\n================================")
print("          BMI REPORT")
print("================================")
print(f"Name: {name}")
print(f"Weight: {weight:.1f} kg")
print(f"Height: {height:.2f} m")
print(f"BMI: {bmi:.2f}")
print("================================")