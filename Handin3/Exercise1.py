import Course
import Student
import DataSheet
import random
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np



def initializeData():
    c1 = Course.Course('course1', 'room1', 'teacher1', 1, grade=10)
    c2 = Course.Course('course2', 'room2', 'teacher2', 1, grade=7)
    c3 = Course.Course('course3', 'room3', 'teacher3', 1, grade=4)
    c4 = Course.Course('course4', 'room4', 'teacher4', 1)

    courses = [c1, c2, c3, c4]
    d = DataSheet.DataSheet(courses)
    s = Student.Student('Student1','Male', 'img', d)
    return s, d


def generateStudentsList(n):
    grades = [-3, 0, 2, 4, 7, 10, 12]
    courseNames = ['Math', 'English', 'Sports', 'Drama', 'Music']
    firstNames = [{'name': 'Elmer', 'gender': 'Male'},
    {'name': 'Zaid', 'gender': 'Male'},
    {'name': 'Brandan', 'gender': 'Male'},
    {'name': 'Damon', 'gender': 'Male'},
    {'name': 'Gregg', 'gender': 'Male'},
    {'name': 'Antoinette', 'gender': 'Female'},
    {'name': 'Joanne', 'gender': 'Female'},
    {'name': 'Alishia', 'gender': 'Female'},
    {'name': 'May', 'gender': 'Female'}]
    lastNames = ['Peel', 'Mcnamara', 'Floyd', 'Freeman', 'Butler', 'Hutton']
    students = []
    for i in range(0, n):
        #Courses
        courses = []
        for j in range(0, random.randrange(1,7)):
            hasGrade = random.randrange(0,2)
            courseName = courseNames[random.randint(0, len(courseNames)-1)]
            if hasGrade == 1:
                c = Course.Course(courseName, 'classRoom', 'teacher', random.randint(5,25), grade=grades[random.randint(0, len(grades)-1)])
            elif hasGrade == 0:
                c = Course.Course(courseName, 'classRoom', 'teacher', 0)
            courses.append(c)
        dataSheet = DataSheet.DataSheet(courses)
        studentFirstName = firstNames[random.randint(0, len(firstNames)-1)]
        studentLastName = lastNames[random.randint(0,len(lastNames)-1)]
        name = studentFirstName['name'] +' '+ studentLastName
        s = Student.Student(name, studentFirstName['gender'], 'URL', dataSheet)
        students.append(s)
    return students

def write_to_CSV(students):
    with open('students.csv', 'w',) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'average', 'progression','courses, ECTS and grades'])
        for s in students:
            courses = []
            for c in s.data_sheet.courses:
                courses.append(c.name)
                courses.append(c.grade)
                courses.append(c.ECTS)
            writer.writerow([s.name, s.get_avg_grade(), s.get_ECTS_progression(), courses])
        
def read_from_CSV():
    students = []
    with open('students.csv', 'r') as csvfile:
        lines = csvfile.readlines()
        for i in range(1, len(lines)):
            student = {}
            if ',' in lines[i]:
                lineSplit = lines[i].split(',')
                student['name'] = lineSplit[0]
                student['avg'] = lineSplit[1]
                student['prog'] = lineSplit[2]
                students.append(student)
    return students

def sort_by_avg(students):
    return sorted(students, key = lambda i: float(i['avg']))

def sort_by_progression(students):
    return sorted(students, key = lambda i: float(i['prog']))

def average_grade_chart(students):
    students = sort_by_avg(students)
    names = []
    grades = []
    for s in students:
        names.append(s['name'])
        grades.append(s['avg'])

    y_pos = np.arange(len(students))
    plt.xticks(y_pos, names)
    plt.bar(y_pos, grades, align='center', alpha=0.5)
    plt.ylabel('Average grade')
    plt.show()

def progression_chart(students):
    students = sort_by_progression(students)
    names = []
    prog = []
    for s in students:
        names.append(s['name'])
        prog.append(s['prog'])

    y_pos = np.arange(len(students))
    plt.xticks(y_pos, names)
    plt.bar(y_pos, prog, align='center', alpha=0.5)
    plt.ylabel('progression')
    plt.show()

if __name__ == '__main__':
    students = generateStudentsList(6)
    write_to_CSV(students)
    students = read_from_CSV()
    #students = sort_by_avg(students)
    #average_grade_chart(students)
    progression_chart(students)