import module_1


class Cart:

    def __init__(self, customer: module_1.Customer = None):
        self.customer = customer
        self.products = []
        self.quantities = []

    def add_product(self, product, quantity: int | float):
        if product in self.products:
            index = self.products.index(product)
            self.quantities[index] += quantity
        else:
            self.products.append(product)
            self.quantities.append(quantity)

    def total(self):
        res = 0
        for index, item in enumerate(self.products):
            res += item.price * self.quantities[index]
        return res

    def __str__(self):
        res = f'{self.customer}\n'

        for index, item in enumerate(self.products):
            res += f'\t{item} x {self.quantities[index]} = {item.price * self.quantities[index]} грн.\n'

        res += f'Total price: {self.total()} грн.'

        return res
