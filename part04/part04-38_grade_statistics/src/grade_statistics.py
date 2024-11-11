# Write your solution here

def user_inputs():
    exam_list = []
    exercise_list = []
    while True:
        string = input("exam_list points and exercises completed: ")
        if string == "":
            return exam_list, exercise_list
        else:
            nums = string.split()
            num1 = int(nums[0])
            num2 = int(nums[1])
            exam_list.append(num1)
            exercise_list.append(int(num2/10))

def total(exam_list: list, exercise_list: list):
    i = 0 
    total_list = []
    while i < len(exam_list):
        fail = 0
        if exam_list[i] < 10:
            fail = 1
        total = 0
        total += exam_list[i] + exercise_list[i]
        total_list.append([total, fail])
        i += 1
    return total_list

def grades(total_list):
    grade_list = []
    for elem in total_list:
        if elem[0] < 15 or elem[1] == 1:
            grade_list.append(0)
        elif elem[0] < 18:
            grade_list.append(1)
        elif elem[0] < 21:
            grade_list.append(2)
        elif elem[0] < 24:
            grade_list.append(3)
        elif elem[0] < 28:
            grade_list.append(4)
        else:
            grade_list.append(5)
    return grade_list

def average(total_list: list):
    avg_sum = 0
    for elem in total_list:
        avg_sum += elem[0]
    average = avg_sum/len(total_list)
    return format(average, ".1f")

def pass_percent(grade_list):
    i = 0
    for elem in grade_list:
        if elem > 0:
            i += 1
    return format(float(i/len(grade_list) * 100), ".1f")

def distribution(grade_list):
    i = 5
    while i >= 0:
        print(str(i) + ": " + "*" * grade_list.count(i), sep="")
        i -= 1

def main():
    ## Helper Functions
    exam_list, exercise_list = user_inputs()  
    # print(exam_list, exercise_list)
    total_list = total(exam_list, exercise_list)
    # print(total_list)
    grade_list = grades(total_list)
    # print(grade_list)
    avg_value = average(total_list)
    # print(average)
    pass_value = pass_percent(grade_list)
    # print(pass_value)
    print("Statistics: ")
    print(f"Points average: {avg_value}")
    print(f"Pass percentage: {pass_value}")
    print(f"Grade distribution: ")
    distribution(grade_list)

main()

    