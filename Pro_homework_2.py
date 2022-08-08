
class Human:

    def __init__(self, name: str, surname: str, patronymic: str, year_of_birth: str):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.year_of_birt = year_of_birth

    def __str__(self):
        return f'{self.surname} {self.name[0]}.{self.patronymic[0]}., {self.year_of_birt}'


class Student(Human):

    def __init__(self, pasport, tiket_id):
        super().__init__(self, name: str)
        self.pasport = pasport
        self.tiket_id = tiket_id

    def __str__(self):
        return f' {self.pasport},{self.tiket_id}'


human_1 = Human('Ivan', 'Ivanov', 'Ivanovich', '2005')
human_2 = Human('Ivan', 'Petrov', 'Petrovich', '2004')

student_1 = Student('258794', '24864')
student_2 = Student('258s94', '24894')


print(human_1)
print(human_2)
