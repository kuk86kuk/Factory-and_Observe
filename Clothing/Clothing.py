from abc import ABC, abstractmethod


'''
Базовый класс Clothing:
    Это абстрактный класс, который определяет общие свойства и методы для всех видов одежды.
    У всех видов одежды есть общие атрибуты: name, size, color, price.
    Метод display_info — это абстрактный метод, который должен быть реализован в подклассах.
'''
class Clothing(ABC):
    def __init__(self, name, size, color, price):
        self.name = name
        self.size = size
        self.color = color
        self.price = price

    @abstractmethod
    def display_info(self):
        pass

'''
Подклассы одежды:
    Мы создаем подклассы для каждого типа одежды: Blouse, Pants, Shoes.
    Каждый подкласс реализует метод display_info, чтобы выводить информацию о конкретном предмете одежды.
'''
class Blouse(Clothing):
    def display_info(self):
        return f"Blouse: {self.name}, Size: {self.size}, Color: {self.color}, Price: ${self.price}"

class Pants(Clothing):
    def display_info(self):
        return f"Pants: {self.name}, Size: {self.size}, Color: {self.color}, Price: ${self.price}"

class Shoes(Clothing):
    def display_info(self):
        return f"Shoes: {self.name}, Size: {self.size}, Color: {self.color}, Price: ${self.price}"