from threading import Thread
import requests


# Теперь потоки в классах.
# Для этого необходимо при создании класса указать, что он наследует класс Threads.
class Getter(Thread):
    res = []
    THE_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre'

    def __init__(self, url):
        self.THE_URL = url
        super().__init__()

    # Метод run из класса Thread.
    # В потоке он 'исполняет' роль target.
    def run(self):
        response = requests.get(self.THE_URL)
        Getter.res.append(response.json())


# Список потоков для удобства.
threads = []
num_of_genres = 10
for i in range(num_of_genres):
    thread = Getter('https://binaryjazz.us/wp-json/genrenator/v1/genre')
    thread.start()
    threads.append(thread)

for thr in threads:
    thr.join()

print(Getter.res)
