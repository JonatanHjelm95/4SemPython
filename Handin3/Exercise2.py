import Exercise1
import NotEnoughStudentsException

def get_students_closest_to_finish(students):
    students = Exercise1.sort_by_progression(students)
    try:
        return students[-1],students[-2],students[-3]
    except Exception as e:
        return 'not enough students'


if __name__ == '__main__':
    students = Exercise1.generateStudentsList(2)
    Exercise1.write_to_CSV(students)
    students = Exercise1.read_from_CSV()
    students = get_students_closest_to_finish(students)
    print(students)
    