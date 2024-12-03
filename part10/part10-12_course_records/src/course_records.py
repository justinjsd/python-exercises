class Course:
    def __init__(self, course: str, grade: int, credits: int):
        self.__course = course
        self.__grade = grade
        self.__credits = credits

    def get_grade(self):
        return int(self.__grade)
    
    def get_credits(self):
        return int(self.__credits)

    def __str__(self):
        return f"{self.__course} ({self.__credits} cr) grade {self.__grade}"

class CourseRecord:
    def __init__(self):
        self.__courses = {}

    def add_course(self, course: str, grade: int, credits: int):
        if course not in self.__courses:
            self.__courses[course] = Course(course, grade, credits)
        else:
            if grade > self.__courses[course].get_grade():
                self.__courses[course] = Course(course, grade, credits)

    def get_course(self, course: str):
        return self.__courses.get(course, None)

    def completed_courses(self):
        return len(self.__courses)

    def total_credits(self):
        return sum(course.get_credits() for course in self.__courses.values())

    def total_grades(self):
        return sum(course.get_grade() for course in self.__courses.values())

    def mean_grade(self):
        if self.completed_courses() == 0:
            return "No Courses"
        return f"{self.total_grades() / self.completed_courses():.1f}"

    def grade_distribution(self):
        grade_dict = {i: 0 for i in range(5, 0, -1)}
        for course in self.__courses.values():
            grade_dict[course.get_grade()] += 1

        for grade, count in grade_dict.items():
            print(f"{grade}: {'x' * count}")

class CourseRecordApplication:
    def __init__(self):
        self.__courses = CourseRecord()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__courses.add_course(course, grade, credits)

    def search(self):
        course = input("course: ")
        course_data = self.__courses.get_course(course)
        if course_data is None:
            print("no entry for this course")
        else:
            print(course_data)

    def statistics(self):
        print(f"{self.__courses.completed_courses()} completed courses, a total of {self.__courses.total_credits()} credits")
        print(f"mean {self.__courses.mean_grade()}")
        print("grade distribution")
        self.__courses.grade_distribution()

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.search()
            elif command == "3":
                self.statistics()
            else:
                self.help()

# Run the application
application = CourseRecordApplication()
application.execute()