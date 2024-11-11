if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam Points: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"

students = {}

with open(student_info) as student_info:
    for student in student_info:
        student = student.split(';')
        if student[0] == "id":
            continue
        students[student[0]] = student[1] + " " + student[2].strip()

exercises = {}
exercises_pts = {}

with open(exercise_data) as exercise_data:
    for exercise in exercise_data:
        exercise = exercise.split(';')
        if exercise[0] == "id":
            continue
        esum = 0
        for i in range(1, 8):
            esum += int(exercise[i])
        exercises[exercise[0]] = esum
        exercises_pts[exercise[0]] = esum//4

examps = {}

with open(exam_points) as exam_points:
    for exam_point in exam_points:
        exam_point = exam_point.split(';')
        if exam_point[0] == "id":
            continue
        esum = 0
        for i in range(1, 4):
            esum += int(exam_point[i])
        examps[exam_point[0]] = esum

for id, student in students.items():
    if id in exercises:
        exercise = exercises[id]
        exercise_point = exercise_point
        exam_point = examps[id]
        total = exercise + exam_point
        if total > -1 and total < 15:
            grade = 0
        elif total > 14 and total < 18:
            grade = 1
        elif total > 17 and total < 21:
            grade = 2
        elif total > 20 and total < 24:
            grade = 3
        elif total > 23 and total < 28:
            grade = 4
        else:
            grade = 5
        print(f"{student} {grade}")
    else:
        print(f"{student}")