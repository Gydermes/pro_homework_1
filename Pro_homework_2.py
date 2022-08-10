
class Human:

    def __init__(self,  surname: str, name: str, patronymic: str, year_of_birth: str):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.year_of_birt = year_of_birth

    def __str__(self):
        return f'{self.surname} {self.name[0]}.{self.patronymic[0]}.,{self.year_of_birt}'


class Student(Human):

    def __init__(self, surname, name, patronymic, year_of_birth, passport, number):
        super().__init__(surname, name, patronymic, year_of_birth)
        self.passport = passport
        self.number = number

    def __str__(self):
        return f' passport{self.passport}, st_number: {self.number}'


class Group(Student):
    def __init__(self, surname: str, name: str, patronymic: str, year_of_birth: str, pas, tik,):
        super().__init__(surname, name, patronymic, year_of_birth, pas, tik)
        self.group = []

    def add_student(self, student: Student):
        group = []
        if student in self.student:
            self.group.append(student)
        if student == student:
            print(group)
        else:
            return 1


human_1 = Human('Ivanov', 'Andreu', 'Ivanovich', '2005')
human_2 = Human('Petrov', 'Petr', 'Petrovich', '2004')
human_3 = Human('Sidorov', 'Ivan', 'Ivanovich', '1988')
human_4 = Human('Sherbina', 'Sergei', 'Petrovich', '2000')
human_5 = Human('Ivashko', 'Ivan', 'Andreevich', '2002')
human_6 = Human('Sherbina', 'Olga', 'Petrovna', '2001')
human_7 = Human('Shevchenko', 'Georgiu', 'Valentinovich', '2000')
human_8 = Human('Abramovich', 'Nata', 'Petrovna', '2004')
human_9 = Human('Lusenko', 'Zlata', 'Ivanovna', '2003')
human_10 = Human('Shevchenko', 'Alex', 'Petrovich', '2004')


student_1 = Student('Ivanov', 'Andreu', 'Ivanovich', '2005', '254s94', '24824')
student_2 = Student('Petrov', 'Petr', 'Petrovich', '2004', '254s94', '24824')
student_3 = Student('Sidorov', 'Ivan', 'Ivanovich', '1988', '858s97', '24834')
student_4 = Student('Sherbina', 'Sergei', 'Petrovich', '2000', '954s94', '24844')
student_5 = Student('Ivashko', 'Ivan', 'Andreevich', '2002', '222s94', '24854')
student_6 = Student('Sherbina', 'Olga', 'Petrovna', '2001', '254s94', '24864')
student_7 = Student('Shevchenko', 'Georgiu', 'Valentinovich', '2000','148s94', '24874')
student_8 = Student('Abramovich', 'Nata', 'Petrovna', '2004', '224s94', '24884')
student_9 = Student('Lusenko', 'Zlata', 'Ivanovna', '2003', '217s94', '24894')
student_10 = Student('Shevchenko', 'Alex', 'Petrovich', '2004','858s94', '24850')

print(human_1, student_1)
print("2.", student_2)
print("5.", student_3)
print("4.", student_4)
print("5.", student_5)
print("6.", student_6)
print("7.", student_7)
print("8.", student_8)
print("9.", student_9)
print("10.", student_10)

