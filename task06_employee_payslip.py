employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary (ETB): "))
transport_allowance = float(input("Enter transport allowance (ETB): "))
food_allowance = float(input("Enter food allowance (ETB): "))

gross_salary = basic_salary + transport_allowance + food_allowance

print("\n========================================")
print("             EMPLOYEE PAYSLIP")
print("========================================")
print(f"Employee: {employee_name}")
print(f"Basic Salary:        \t{basic_salary:.2f} ETB")
print(f"Transport Allowance: \t{transport_allowance:.2f} ETB")
print(f"Food Allowance:      \t{food_allowance:.2f} ETB")
print("----------------------------------------")
print(f"Gross Salary:        \t{gross_salary:.2f} ETB")
print("========================================")