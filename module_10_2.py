from time import sleep
from threading import Thread


class Knight(Thread):

    def __init__(self, name, power, enemys=100):
        super().__init__()
        self.name = name
        self.power = power
        self.enemys = enemys


    def run(self):
        print(f'{self.name}, на нас напали!')
        number_enemys = self.enemys
        number_days = 0
        while number_enemys > 0:
            number_enemys -= self.power
            number_days += 1
            print(f'{self.name} сражается {number_days} день(дня)..., '
                  f'осталось {number_enemys} врагов.')
            sleep(1.0)
        print(f'{self.name} одержал победу спустя {number_days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

knighs_in_fights = []
first_knight.start()
knighs_in_fights.append(first_knight)
second_knight.start()
knighs_in_fights.append(second_knight)

for knight in knighs_in_fights:
    knight.join()

print('Все битвы закончились!')
