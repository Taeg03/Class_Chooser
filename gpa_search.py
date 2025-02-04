"""
This script will search for the average GPA of a list of classes and print them in descending order.
"""

import planetterp

def get_course_gpa(course_name):
    course = planetterp.course(name=course_name)
    return course.get('average_gpa', 0)

classes = ["ENEE460", "ENEE313", "ENEE380", "ENEE382", "ENEE413", "ENEE426", "ENEE436", "ENEE439G", "ENEE440", "ENEE459C", "ENEE459V", "ENEE463", "ENEE469O", "ENEE475", "ENEE489L", "ENEE489Q", "ENEE496"]
course_gpas = []

for course in classes:
    gpa = get_course_gpa(course)
    course_gpas.append((course, gpa))

sorted_classes = sorted(course_gpas, key=lambda x: x[1], reverse=True)

for course, gpa in sorted_classes:
    print(f"{course}: {gpa}")