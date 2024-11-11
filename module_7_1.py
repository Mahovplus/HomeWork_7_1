from pprint import pprint as pp

class Product:
    """Инициализация характеристик продуктов."""

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        """Вывод характеристик в консоль, в строковом формате"""
        return f"{self.name}, {self.weight}, {self.category}."

class Shop:
    """TranceProducts inc"""

    __file_name  = "products.txt"

    def get_products(self):
        file = open(self.__file_name, 'r')
        read = file.read()
        file.close()
        return read

    def add(self, *products):
            for product in products:
                if str(product) in self.get_products():
                    print(f"Продукт {product} уже есть в магазине.")
                else:
                    file = open(self.__file_name, 'a')
                    file.seek(0)
                    file.write(f'{product}\n')
                    file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())

