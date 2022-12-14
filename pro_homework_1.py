import module_1
import module_2


class Product:

    def __init__(self, title: str, price: int | float):
        if not isinstance(title, str):
            raise TypeError()
        self.title = title
        if not isinstance(price, int | float):
            raise TypeError()
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price} грн.'


# class Customer:
#
#     def __init__(self, name: str, surname: str, phone: str):
#         if not isinstance(name, str):
#             raise TypeError()
#         self.name = name
#         if not isinstance(surname, str):
#             raise TypeError()
#         self.surname = surname
#         if not isinstance(phone, str):
#             raise TypeError()
#         self.phone = phone
#
#     def __str__(self):
#         return f'{self.surname} {self.name[0]}., {self.phone}'


# class Cart:
#
#     def __init__(self, customer: Customer = None):
#         self.customer = customer
#         self.products = []
#         self.quantities = []
#
#     def add_product(self, product: Product, quantity: int | float):
#         if product in self.products:
#             index = self.products.index(product)
#             self.quantities[index] += quantity
#         else:
#             self.products.append(product)
#             self.quantities.append(quantity)
#
#     def total(self):
#         res = 0
#         for index, item in enumerate(self.products):
#             res += item.price * self.quantities[index]
#         return res
#
#     def __str__(self):
#         res = f'{self.customer}\n'
#
#         for index, item in enumerate(self.products):
#             res += f'\t{item} x {self.quantities[index]} = {item.price * self.quantities[index]} грн.\n'
#
#         res += f'Total price: {self.total()} грн.'
#
#         return res



pr_1 = Product('banana', 45)
pr_2 = Product('apple', 21)
pr_3 = Product('orange', 22)

customer_1 = module_1.Customer('Ivan', 'Ivanov', '123456789')
customer_2 = module_1.Customer('Ivan', 'Petrov', '223456789')

order_1 = module_2.Cart(customer_1)
order_2 = module_2.Cart(customer_2)

order_1.add_product(pr_1, 2.5)
order_1.add_product(pr_2, 3.)
order_1.add_product(pr_1, 2)
order_2.add_product(pr_1, 1)
order_2.add_product(pr_2, 1)
order_2.add_product(pr_3, 1)
print(customer_2)
print(order_1)
print(order_1.customer)
print(order_1)
print(order_1.quantities)
print(order_2)