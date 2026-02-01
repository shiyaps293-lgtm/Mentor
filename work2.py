# Student Result Processing System

# Function to input marks
def input_marks():
    marks = []
    n = int(input("Enter number of subjects: "))
    for i in range(n):
        m = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)
    return marks

# Function to calculate total and average
def calculate_total_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

# Function to assign grade
def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# Function to display result
def display_result(marks, total, average, grade):
    print("\n--- Student Result ---")
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)

# Main program
marks = input_marks()
total, average = calculate_total_average(marks)
grade = assign_grade(average)
display_result(marks, total, average, grade)