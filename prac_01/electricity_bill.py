TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

customer_tariff = float(input("Which tariff? 11 or 31: "))
if customer_tariff == 11:
    customer_tariff = TARIFF_11
elif customer_tariff == 31:
    customer_tariff = TARIFF_31
else:
    print("Invalid Input: Please try again")
    customer_tariff = float(input("Which tariff? 11 or 31: "))

daily_use = float(input("Enter daily use in kWh: "))
while daily_use < 0 or daily_use > 24:
    print("Invalid Input: Please try again")
    daily_use = float(input("Enter daily use in kWh: "))


billing_days = float(input("Enter number of billing days: "))
while billing_days < 0 or billing_days > 90:
    print("Invalid Input: Please try again")
    billing_days = float(input("Enter number of billing days: "))

estimated_bill = customer_tariff * daily_use * billing_days

print("Estimated Bill: ", estimated_bill)
