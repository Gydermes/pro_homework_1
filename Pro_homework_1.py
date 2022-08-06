class Phone:

    def __init__(self, model, color, year):

        self.model = model
        self.color = color
        self.year = year

    def __str__(self):

        return f'{self.model}, {self.color}, {self.year}'


phone_1 = Phone("Iphone", "white", 2020)
phone_2 = Phone("Samsung", "red", 2019)

print(phone_1, phone_2, sep="\n")


class Buyer:
    def __init__(self, surname, name, patronymic, phone_number):

        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone_number = phone_number

    def __str__(self):

        return f'{self.surname}, {self.name}, {self.patronymic}, {self.phone_number}'


buyer_1 = Buyer("Ivanov", "Ivan", "Ivanovich", "+380933344444")


print(buyer_1)