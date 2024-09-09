from threading import Thread
from time import sleep
from random import randint
import queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, guest_name):
        super().__init__()
        self.name = guest_name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        count_g = 0
        for guest in guests:
            count_g += 1
            for table in self.tables:
                if count_g <= len(self.tables) and table.guest == None:
                    table.guest = guest
                    print(f'{guest.name} сел за стол номер {table.number}.')
                    table.guest.start()
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди.')

    def discuss_guests(self):
        while not self.queue.empty() or any([table.guest for table in self.tables]):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-ла) и ушёл(-ла).')
                    print(f'Стол номер {table.number} свободен.')
                    table.guest.join()
                    table.guest = None
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-ла) за стол номер {table.number}.')
                        table.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
