import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(file.readline())
            if not line:
                break


filenames = [f'file {number}.txt' for number in range(1, 5)]

# Линейный вызов.
start = datetime.datetime.now()
for filename in filenames:
    read_info(filename)
end = datetime.datetime.now()
print(end - start)


# Многопроцессный вызов.
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start)