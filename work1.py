# Employee Salary Calculator System

def input_employee_details():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))
    return emp_id, name, basic_salary


def calculate_gross_salary(basic_salary):
    hra = basic_salary * 0.20      # 20% HRA
    da = basic_salary * 0.10       # 10% DA
    gross_salary = basic_salary + hra + da
    return gross_salary, hra, da


def calculate_deductions(gross_salary):
    pf = gross_salary * 0.12       # 12% PF
    tax = gross_salary * 0.05      # 5% Tax
    total_deductions = pf + tax
    return total_deductions, pf, tax


def display_final_salary(emp_id, name, basic, gross, deductions):
    net_salary = gross - deductions
    print("\n----- Employee Salary Details -----")
    print("Employee ID   :", emp_id)
    print("Employee Name :", name)
    print("Basic Salary  :", basic)
    print("Gross Salary  :", gross)
    print("Deductions    :", deductions)
    print("Net Salary    :", net_salary)


# Main Program
emp_id, name, basic_salary = input_employee_details()
gross_salary, hra, da = calculate_gross_salary(basic_salary)
deductions, pf, tax = calculate_deductions(gross_salary)
display_final_salary(emp_id, name, basic_salary, gross_salary, deductions)