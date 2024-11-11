# Write your solution here
import urllib.request
import json
from math import *

def retrieve_all():
    url_list = []
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    url_jsons = json.loads(my_request.read())
    for url_json in url_jsons:
        if url_json["enabled"] == True:
            url_list.append((url_json["fullName"], url_json["name"], url_json["year"], sum(url_json["exercises"])))
    return url_list

def retrieve_course(course_name: str):
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = my_request.read()
    course = json.loads(data)
    course_info = {}
    weeks = 0
    students = 0
    hours = 0
    exercises = 0
    for week, data in course.items():
        weeks += 1
        if data['students'] > students:
            students = data['students']
        hours += data['hour_total']
        exercises += data['exercise_total']
    hours_average = floor(hours/students)
    exercises_average = floor(exercises/students)

    course_info['weeks'] = weeks
    course_info['students'] = students
    course_info['hours'] = hours
    course_info['hours_average'] = hours_average
    course_info['exercises'] = exercises
    course_info['exercises_average'] = exercises_average

    return course_info


# print(retrieve_all())
# print(retrieve_course("docker2019"))
