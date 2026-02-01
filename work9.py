# Function to validate answers
def validate_answers(correct_answers, student_answers):
    results = []
    for i in range(len(correct_answers)):
        if student_answers[i] == correct_answers[i]:
            results.append(True)
        else:
            results.append(False)
    return results


# Function to calculate score
def calculate_score(results):
    score = 0
    for res in results:
        if res:
            score += 1
    return score


# Function to generate grade
def generate_grade(score, total):
    percentage = (score / total) * 100

    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"


# Main program
correct_answers = ['A', 'B', 'C', 'D', 'A']
student_answers = []

print("Enter your answers:")
for i in range(len(correct_answers)):
    ans = input(f"Question {i+1}: ").upper()
    student_answers.append(ans)

results = validate_answers(correct_answers, student_answers)
score = calculate_score(results)
grade = generate_grade(score, len(correct_answers))

print("\nResults")
print("Score:", score, "/", len(correct_answers))
print("Grade:", grade)