key_to_check = "Bob"
key_exists = key_to_check in student_grades
print(f"Does the key '{key_to_check}' exist?:", key_exists)
student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
new_student = "David"
new_grade = 92
student_grades[new_student] = new_grade
print("Updated Dictionary:", student_grades)
