import multiprocessing, datetime


def read_info(name: str) -> None:
    all_data = []
    with open(name) as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()


# start = datetime.datetime.now()
# for number in range(1, 5):
#    read_info(f'./files/file {number}.txt')
# end = datetime.datetime.now()
# print(end - start)


if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        filenames = [f'./files/file {number}.txt' for number in range(1, 5)]
        start = datetime.datetime.now()
        pool.map(read_info, filenames)
        end = datetime.datetime.now()
        print(end - start)
# 0:00:04.595926 - Линейный вызов
# 0:00:01.724643 - Многопроцессный
