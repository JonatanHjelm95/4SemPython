import Exercise1
import matplotlib.pyplot as plt

def create_ECTS_pie_chart(students):
    names = []
    ECTSs = []
    for s in students:
        names.append(str(s['name']).replace(' ',''))
        ECTSs.append(s['prog'])
    print(names)
    labels = list(names)
    sizes = list(ECTSs)
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'green', 'grey', 'orange']
    #explode = (0.1, 0, 0, 0)  # explode 1st slice

    # Plot
    plt.pie(sizes, labels=names, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()


if __name__ == '__main__':
    students = Exercise1.generateStudentsList(6)
    Exercise1.write_to_CSV(students)
    students = Exercise1.read_from_CSV()

    create_ECTS_pie_chart(students)
    