class Shop:

    def __init__(self, technique, model, price):

        self.technique = technique
        self.model = model
        self.price = price

    def __str__(self):

        return f'{self.technique}, {self.model},{self.price}$'


class Buyer:
    def __init__(self, surname, name, patronymic, phone_number):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone_number = phone_number

    def __str__(self):

        return f'{self.surname} {self.name[0]}.{self.patronymic[0]}., {self.phone_number}'


product_1 = Shop("Phone", "Iphone", 200)
product_2 = Shop("TV", "Samsung", 105)
buyer_1 = Buyer("Ivanov", "Ivan", "Ivanovich", "+380933344444")

print(buyer_1, "Product :", product_1, product_2, sep="\n")
