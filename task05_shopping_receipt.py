customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
price = float(input("Enter product price (ETB): "))
quantity = int(input("Enter quantity: "))

total_price = price * quantity

print("\n==========================================")
print("              RECEIPT")
print("==========================================")
print(f"Customer: {customer_name}")
print("Product\t\tPrice\t\tQty")
print("------------------------------------------")
print(f"{product_name}\t\t{price:.2f}\t\t{quantity}")
print(f"\nTotal: {total_price:.2f} ETB")
print("Thank you for shopping!")
print("==========================================")