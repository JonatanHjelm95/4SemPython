

class Course:
    def __init__(self, name, classRoom, teacher, ECTS, **grade):
        self.name = name
        self.classRoom = classRoom
        self.teacher = teacher
        self.ECTS = ECTS
        self.grade = grade