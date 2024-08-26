from time import sleep
from threading import Thread
from datetime import datetime


def wite_words(word_count, file_name):
    with open(file_name, 'w+', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}.')


time_start_func = datetime.now()
res1 = wite_words(10, 'example1.txt')
res2 = wite_words(30, 'example2.txt')
res3 = wite_words(200, 'example3.txt')
res4 = wite_words(100, 'example4.txt')
time_end_func = datetime.now()
print(f'Работа потоков (время записи в файлы с помощью функции и цикла): {time_end_func - time_start_func}.')

first_thread = Thread(target=wite_words, args=(10, 'example1.txt'))
second_thread = Thread(target=wite_words, args=(30, 'example2.txt'))
third_thread = Thread(target=wite_words, args=(200, 'example3.txt'))
fourth_thread = Thread(target=wite_words, args=(100, 'example4.txt'))

time_start_threads = datetime.now()
first_thread.start()
second_thread.start()
third_thread.start()
fourth_thread.start()

first_thread.join()
second_thread.join()
third_thread.join()
fourth_thread.join()
time_end_threads = datetime.now()
print(f'Работа потоков (время записи в файлы с помощью потоков): {time_end_threads - time_start_threads}.')
