from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        for i in self.users:
            if nickname == i.nickname:
                print(f'Пользователь {nickname} уже существует.')
                break
        else:
            new_user = User(nickname, hash(password), age)
            self.users.append(new_user)
            self.log_in(new_user.nickname, password)

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname == i.nickname:
                if hash(password) == i.password:
                    self.current_user = i
                    print(f'Приветствую вас, {i.nickname}')
                    break
                else:
                    print('Неверный пароль!')
                    break
        else:
            print('Такого пользователя не найдено!')

    def log_out(self):
        print(f'Прощайте пользователь, {self.current_user.nickname}')
        self.current_user = None

    def add(self, *args):
        for new_video in args:
            for video in self.videos:
                if new_video == video:
                    break
            else:
                self.videos.append(new_video)

    def get_videos(self, sub_title):
        list_videos = []
        for video in self.videos:
            if sub_title.lower() in video.title.lower():
                list_videos.append(video.title)
        return list_videos

    def watch_video(self, title):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for video in self.videos:
                if title == video.title:
                    if self.current_user.age < 18 and video.adult_mode == True:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        video.time_now = video.time_now if video.time_now != 0 else 1
                        for i in range(video.time_now, video.duration + 1):
                            sleep(1)
                            print(i, end=' ')
                        print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# ur.log_out()
# print(ur.current_user)
# ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
# print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
