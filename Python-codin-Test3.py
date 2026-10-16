students_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve": 88
}

print("Student Marks:", students_marks)

for student, marks in students_marks.items():
    average_marks = sum(students_marks.values())

print(f"The average marks of the students is: {average_marks / len(students_marks)}")

print("Lowest Marks and Highest marks respectively are:", min(students_marks.values()), max(students_marks.values()))
try:
    student_name = input("Enter the name of the student to get their marks: ")
    if student_name in students_marks:
        print(f"{student_name}'s marks are: {students_marks[student_name]}")
    else:
        print(f"{student_name} is not found in the records.")
except KeyError:
    input("Invalid input. Please enter a valid student name.")
else: 
    print("Thank you for using the student marks program.")