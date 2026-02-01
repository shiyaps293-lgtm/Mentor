# Payroll Management System

employees = {}

# Function to add employee data
def add_employee(emp_id, name, basic_salary):
    employees[emp_id] = {
        "name": name,
        "basic": basic_salary
    }
    print("Employee added successfully.")

# Function to calculate salary dynamically
def calculate_salary(basic, hra_rate=0.20, da_rate=0.10):
    hra = basic * hra_rate
    da = basic * da_rate
    gross_salary = basic + hra + da
    return gross_salary

# Function to handle bonus and deductions
def apply_bonus_deductions(gross, bonus=0, deduction=0):
    net_salary = gross + bonus - deduction
    return net_salary

# Function to generate payroll report
def generate_payroll_report():
    print("\n--- Payroll Report ---")
    for emp_id, data in employees.items():
        gross = calculate_salary(data["basic"])
        net = apply_bonus_deductions(gross)
        print("Employee ID:", emp_id)
        print("Name:", data["name"])
        print("Basic Salary:", data["basic"])
        print("Gross Salary:", gross)
        print("Net Salary:", net)
        print()

# Main program
while True:
    print("\n1. Add Employee")
    print("2. Generate Payroll Report")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        basic = float(input("Enter basic salary: "))
        add_employee(emp_id, name, basic)

    elif choice == '2':
        generate_payroll_report()

    elif choice == '3':
        print("Exiting Payroll System.")
        break

    else:
        print("Invalid choice.")