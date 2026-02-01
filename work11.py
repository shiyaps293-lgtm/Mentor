# Core billing function
def calculate_bill(amount, tax_function):
    tax = tax_function(amount)
    total_amount = amount + tax
    return tax, total_amount


# Tax calculation functions (can be extended easily)
def india_tax(amount):
    return amount * 0.18   # 18% GST


def usa_tax(amount):
    return amount * 0.10   # 10% Sales Tax


def uk_tax(amount):
    return amount * 0.20   # 20% VAT


# Main program
amount = float(input("Enter base amount: "))
region = input("Enter region (India/USA/UK): ").lower()

# Select tax function dynamically
if region == "india":
    tax_func = india_tax
elif region == "usa":
    tax_func = usa_tax
elif region == "uk":
    tax_func = uk_tax
else:
    print("Invalid region")
    exit()

tax, total = calculate_bill(amount, tax_func)

print("\nBilling Details")
print("Base Amount:", amount)
print("Tax:", tax)
print("Total Bill:", total)