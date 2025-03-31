## You have access to a database of student_scores in the format of a dictionary. 
# The keys in student_scores are the names of the students and the values are their exam scores. 

# Write a program that converts their scores to grades.
# By the end of your program, you should have a new dictionary called student_grades that should 
# contain student names as keys and their assessed grades for values. 

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# lets make a little grading func
def grade(score):
    if score > 90:
        return "Outstanding"
    elif score > 80:
        return "Exceeds Expectations"
    elif score > 70:
        return "Acceptable"
    else:
        return "Fail"

student_grades = {}

# for each student (key) make a clone key to the new dictionary
# set its value to the grade their score deserves
for student in student_scores:
    student_grades[student] = grade(student_scores[student])
    print(f"{student}: {student_grades[student]}")
