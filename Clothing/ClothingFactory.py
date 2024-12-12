from Clothing.Clothing import Blouse, Pants, Shoes


'''
Фабрика ClothingFactory:
    это класс, который создает объекты одежды.
    Метод create_clothing принимает тип одежды (Blouse, Pants, Shoes) и параметры для создания объекта.
    В зависимости от типа одежды, фабрика создает соответствующий объект.
'''
class ClothingFactory:
    @staticmethod
    def create_clothing(clothing_type, name, size, color, price):
        if clothing_type == "Blouse":
            return Blouse(name, size, color, price)
        elif clothing_type == "Pants":
            return Pants(name, size, color, price)
        elif clothing_type == "Shoes":
            return Shoes(name, size, color, price)
        else:
            raise ValueError(f"Unknown clothing type: {clothing_type}")