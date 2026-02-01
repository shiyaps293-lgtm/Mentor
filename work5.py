# Employee Attendance Management System

attendance = {}

# Function to mark attendance
def mark_attendance():
    name = input("Enter employee name: ")
    status = input("Enter attendance (P/A): ").upper()
    if status == 'P':
        attendance[name] = attendance.get(name, 0) + 1
        print("Attendance marked as Present.")
    elif status == 'A':
        attendance.setdefault(name, attendance.get(name, 0))
        print("Attendance marked as Absent.")
    else:
        print("Invalid input. Use P or A.")

# Function to calculate working days
def calculate_working_days():
    days = int(input("Enter total working days: "))
    return days

# Function to generate attendance report
def generate_report(total_days):
    print("\n--- Attendance Report ---")
    for name, present_days in attendance.items():
        print("Employee:", name)
        print("Present Days:", present_days)
        print("Absent Days:", total_days - present_days)
        print()

# Main program
total_days = calculate_working_days()

while True:
    print("\n1. Mark Attendance")
    print("2. Generate Report")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        mark_attendance()
    elif choice == '2':
        generate_report(total_days)
    elif choice == '3':
        print("Exiting Attendance System.")
        break
    else:
        print("Invalid choice.")