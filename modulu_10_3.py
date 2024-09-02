import threading
from threading import Thread, Lock
from time import sleep
from random import randint


class Bank(Thread):

    def __init__(self):
        super().__init__()
        self.balanse = int()
        self.lock = threading.Lock()

    def deposit(self, max_adj_transactions=100):
        self.max_adj_transactions = max_adj_transactions
        transactions_number = 0  # Счётчик транзакций пополнения.
        while transactions_number < self.max_adj_transactions:
            if self.balanse >= 500 and self.lock.locked() == True:
                self.lock.release()
            adjunction = randint(50, 500)
            self.balanse += adjunction
            transactions_number += 1
            sleep(0.001)
            print(f'Пополнение: {adjunction}. Баланс: {self.balanse}.', end='\n', flush=True)

    def take(self, max_withdr_transactions=100, max_failure=10):
        self.max_withdr_transactions = max_withdr_transactions
        self.max_failure = max_failure  # Допустимое количество непрерывных отказов.
        transactions_number = 0  # Счётчик транзакций снятия.
        failure_counter = 0  # Счётчик непрерывных отказов.
        while transactions_number < self.max_withdr_transactions:
            withdrawal = randint(50, 500)
            if self.balanse >= withdrawal:
                transactions_number += 1
                failure_counter = 0
                self.balanse -= withdrawal
                sleep(0.00091)
                print(f'Запрос на {withdrawal}. Снятие: {withdrawal}. Баланс: {self.balanse}.', end='\n', flush=True)
            else:
                if failure_counter == 0:
                    failure_counter += 1
                    print(f'Запрос на {withdrawal}. Запрос отклонён, недостаточно средств.', end='\n', flush=True)
                    if self.lock.locked() == False:
                        self.lock.acquire()
                    sleep(0.00064)
                elif failure_counter in range(1, max_failure - 1):
                    failure_counter += 1
                    print(f'Запрос на {withdrawal}. Запрос отклонён, недостаточно средств.', end='\n', flush=True)
                    sleep(0.00058)
                else:
                    print(f'Превышен лимит запросов на снятие. Вы можете снять не больше остатка: {self.balanse}.')
                    break

    def __repr__(self):
        return ''.format(self.balanse)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balanse}.')
