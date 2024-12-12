from abc import ABC, abstractmethod


'''
Абстрактный класс Observer:
    Это базовый класс для всех наблюдателей.
    У него есть метод update, который вызывается, когда происходит событие.
'''
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


'''
Класс Customer:
    Это конкретный наблюдатель, который реализует метод update.
'''
class Customer(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received a notification: {message}")



'''
ClothingStore:
    Это Класс, который управляет наблюдателями.
    У него есть список наблюдателей (_observers), которые подписаны на уведомления.
    Методы attach и detach добавляют и удаляют наблюдателей.
    Метод notify отправляет сообщение всем наблюдателям.
'''
class ClothingStore:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

    def announce_sale(self, message):
        self.notify(message)

    def announce_new_collection(self, message):
        self.notify(message)