import DataSheet

class Student:
    def __init__(self, name, gender, image_url, data_sheet,):
        self.name = name
        self.gender = gender
        self.image_url = image_url
        self.data_sheet = data_sheet
    
    def get_avg_grade(self):
        gradesList = self.data_sheet.get_grades_as_list()
        grades = []
        for i in range(len(gradesList)):
            try:
                grades.append(gradesList[i]['grade'])
                
            except: 
                'no grade is present'
        try:
            return round(sum(grades)/len(grades), 2)
        except:
            return float(0)

    def get_ECTS_progression(self):
        ECTSs = []
        for c in self.data_sheet.courses:
            ECTSs.append(c.ECTS)
        return sum(ECTSs)*150/100