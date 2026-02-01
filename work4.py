# Online Shopping Cart System

cart = {}

# Function to add items
def add_item():
    item = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))
    cart[item] = price * quantity
    print("Item added to cart.")

# Function to remove items
def remove_item():
    item = input("Enter item name to remove: ")
    if item in cart:
        del cart[item]
        print("Item removed from cart.")
    else:
        print("Item not found in cart.")

# Function to calculate total bill
def calculate_total():
    total = sum(cart.values())
    return total

# Function to apply discount
def apply_discount(total):
    discount = 0
    if total >= 1000:
        discount = total * 0.10   # 10% discount
    return total - discount

# Main program
while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Calculate Bill")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        total = calculate_total()
        final_amount = apply_discount(total)
        print("Total Bill:", total)
        print("Final Amount after Discount:", final_amount)
    elif choice == '4':
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice. Try again.")