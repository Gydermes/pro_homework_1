import settings


class MaxStudentsError(Exception):


    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return f'{self.msg}\n{super().__str__()}'

 class Group:

    def __init__(self, title):
        self.title = title
        self.students = []

    def add_student(self, student):
        if len(self.students) >= settings.MAX_STUDENTS_IN_GROUP:
            raise MaxStudentsError('Too many student in group!')

        for item in self.students:
            if item == student:
                return -2

        self.students.append(student)

    def search(self, surname):
        for item in self.students:
            if item.surname.lower() == surname.lower():
                return item

        return 'С такой фамилией студента нет!'

    def __str__(self):
        return f'{self.title}\n' + '\n'.join(map(str, self.students))
