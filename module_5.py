class Person:

    def __init__(self, surname, name):
        if not isinstance(surname, str):
            raise TypeError()
        if not isinstance(name, str):
            raise TypeError()
        self.surname = surname
        self.name = name

    def __str__(self):
        return f'{self.surname} {self.name}'





