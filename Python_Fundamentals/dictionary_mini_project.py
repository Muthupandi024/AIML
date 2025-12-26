student = {}
subject = input("Enter the subject name: ")
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    mark = int(input("Enter mark (0–100): "))

    if 0 <= mark <= 100:
        if name not in student:
            student[name] = mark
        else:
            print(f"{name} already exists!")
    else:
        print("Invalid mark! Enter between 0 and 100")

print("\nStudent Data:", student)
total_marks = 0
for s in student:
    total_marks += student[s]
student_count = len(student)
average = total_marks / student_count
print("\nTotal Marks:", total_marks)
print("Average Mark:", average)
if average >= 45:
    print("Class Result: PASS")
else:
    print("Class Result: FAIL")
if average < 60:
    print(f"Subject Difficulty: {subject} is DIFFICULT")
else:
    print(f"Subject Difficulty: {subject} is EASY")
print("\nStudent-wise Result:")
for name in student:
    if student[name] >= 45:
        print(name, " PASS")
    else:
        print(name, "FAIL")
