def scoreToGrade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def computeGrades(scores):
    grades = [scoreToGrade(score) for score in scores]
    return grades

# Example usage:
student_scores = [85, 92, 78, 60, 72]  # Replace this with the list of students' scores

#student_scores = int (input('Please enter the score: '))
student_grades = computeGrades(student_scores)
# Displaying the results
for i in range(len(student_scores)):
    print(f"Student {i+1}: Score = {student_scores[i]}, Grade = {student_grades[i]}")