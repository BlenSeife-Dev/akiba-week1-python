exchange_rate = 150.0  # 1 USD = 150 ETB

usd_amount = float(input("USD Amount: "))

etb_amount = usd_amount * exchange_rate

print("\n==============================")
print("      CURRENCY EXCHANGE")
print("==============================")
print(f"USD Amount: {usd_amount:.2f}")
print(f"Exchange Rate: 1 USD = {exchange_rate:.0f} ETB")
print(f"ETB Amount: {etb_amount:,.2f} ETB")
print("==============================")