class Customer:

    def __init__(self, name: str, surname: str, phone: str):
        if not isinstance(name, str):
            raise TypeError()
        self.name = name
        if not isinstance(surname, str):
            raise TypeError()
        self.surname = surname
        if not isinstance(phone, str):
            raise TypeError()
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name[0]}., {self.phone}'
