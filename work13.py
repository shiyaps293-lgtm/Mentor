# -------- Calculator Functions --------
def calculator():
    print("\n--- Calculator ---")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    ch = int(input("Choose operation: "))

    if ch == 1:
        print("Result:", a + b)
    elif ch == 2:
        print("Result:", a - b)
    elif ch == 3:
        print("Result:", a * b)
    elif ch == 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Division by zero not allowed")
    else:
        print("Invalid choice")


# -------- String Operations --------
def string_operations():
    print("\n--- String Operations ---")
    s = input("Enter a string: ")

    print("1. Length of string")
    print("2. Reverse string")
    print("3. Uppercase")
    print("4. Lowercase")

    ch = int(input("Choose operation: "))

    if ch == 1:
        print("Length:", len(s))
    elif ch == 2:
        print("Reversed:", s[::-1])
    elif ch == 3:
        print("Uppercase:", s.upper())
    elif ch == 4:
        print("