from Clothing.ClothingFactory import ClothingFactory
from Observer.Observer import ClothingStore, Customer


'''
Фабрика и Наблюдатель в онлайн-магазине одежды:
   - Опишите классы для представления одежды (блузы, брюки, обувь и т.д.).
   - Создайте фабрику для производства конкретных товаров одежды.
   - Используйте наблюдателей для уведомления клиентов о распродажах и новых коллекциях.
'''
 
 

# Создаем фабрику
factory = ClothingFactory()
blouse = factory.create_clothing("Blouse", "Silk Blouse", "M", "White", 50)
pants = factory.create_clothing("Pants", "Nike", "32", "Blue", 70)
shoes = factory.create_clothing("Shoes", "adidas", "42", "Black", 100)

# Выводим информацию о предметах одежды
print(blouse.display_info())
print(pants.display_info())
print(shoes.display_info())

# Создаем магазин и клиентов
store = ClothingStore()
customer1 = Customer("Alice")
customer2 = Customer("Bob")
store.attach(customer1)
store.attach(customer2)

# Уведомляем клиентов о распродаже
store.announce_sale("Большая распродажа! Скидка до 50% на все товары!")

# Уведомляем клиентов о новой коллекции
store.announce_new_collection("Новая осенняя коллекция уже в продаже!")