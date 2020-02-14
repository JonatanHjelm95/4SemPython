import Exercise1
import matplotlib.pyplot as plt

def create_ECTS_pie_chart(students):
    names = []

    for s in students:
        names.append(str(s['name']).replace(' ',''))
    print(names)
    labels = list(names)
    sizes = [215, 130, 245, 210]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0, 0)  # explode 1st slice

    # Plot
    plt.pie(sizes, explode=explode, labels=names, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()


if __name__ == '__main__':
    students = Exercise1.generateStudentsList(2)
    Exercise1.write_to_CSV(students)
    students = Exercise1.read_from_CSV()

    create_ECTS_pie_chart(students)
    