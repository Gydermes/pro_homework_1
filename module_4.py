class Student(Person):

    def __init__(self, surname: str, name: str, date_of_birth: str):
        super().__init__(surname, name)
        if not isinstance(date_of_birth, str):
            raise TypeError()
        self.date_of_birth = date_of_birth

    def __eq__(self, other):
        return self.surname == other.surname and self.name == other.name and self.date_of_birth == other.date_of_birth

    def __str__(self):
        return f'{super().__str__()}; {self.date_of_birth}'
