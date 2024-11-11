# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

students = {}

with open(student_info) as student_info:
    for student in student_info:
        student = student.split(';')
        if student[0] == "id":
            continue
        students[student[0]] = student[1] + " " + student[2].strip()

exercises = {}

with open(exercise_data) as exercise_data:
    for exercise in exercise_data:
        exercise = exercise.split(';')
        if exercise[0] == "id":
            continue
        exercises[exercise[0]] = int(exercise[1]) +int(exercise[2]) +int(exercise[3]) +int(exercise[4])+int(exercise[5]) +int(exercise[6])+int(exercise[7])

for id, student in students.items():
    if id in exercises:
        exercise = exercises[id]
        print(f"{student} {exercise}")
    else:
        print(f"{student}")