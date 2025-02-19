from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(credits: list):
    return reduce(lambda reduced_credit, course: reduced_credit + course.credits, credits, 0)

def sum_of_passed_credits(credits: list):
    return reduce(lambda reduced_credit, course: reduced_credit + course.credits, list(filter(lambda c: c.grade >=1 ,credits)), 0)

def average(attempts: list):
    a = list(filter(lambda x: x.grade>0,attempts))
    return reduce(lambda grades, course: grades + course.grade, a, 0)/len(a)

if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)