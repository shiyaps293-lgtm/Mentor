# Electricity Bill Calculation System

# Function to input units consumed
def input_units():
    units = int(input("Enter units consumed: "))
    return units

# Function to calculate bill using slab rates
def calculate_bill(units):
    bill = 0

    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = (100 * 1.5) + ((units - 100) * 2.5)
    elif units <= 300:
        bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)
    else:
        bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + ((units - 300) * 5)

    return bill

# Function to generate bill summary
def generate_bill_summary(units, bill):
    print("\n--- Electricity Bill Summary ---")
    print("Units Consumed:", units)
    print("Total Bill Amount: ₹", bill)

# Main program
units = input_units()
bill_amount = calculate_bill(units)
generate_bill_summary(units, bill_amount)