import Course

class DataSheet:
    def __init__(self, courses):
        
        self.courses = []
        for c in courses:
            self.courses.append(c)

    def get_grades_as_list(self):
        grades = []
        courses = self.courses
        for c in courses:
            grades.append(c.grade)
        return grades