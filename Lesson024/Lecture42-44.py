class DataBase:

    def __init__(self):
        self.data = {}

    def add_user_to_database(self, username, password):
        self.data[username] = password


class User:
    """
Класс пользователя, содержащий атрибуты: логин, пароль.
Это описание можно вызвать командой User.__doc__.
    """
    def __init__(self):
        self.username = None
        self.password = None

    def create_user(self):
        while True:
            username = input('Введите логин (он должен состоять из 5 до 10 символов): ')
            if 4 < len(username) <= 10:
                break
            else:
                print('Некорректный логин!')

        while True:
            password = input('Введите пароль (он должен состоять из 8 до 20 символов '
                             'и должен содержать хотя бы одну букву и хотя бы одну цифру): ')
            if (7 < len(password) <= 20 and password.isalnum() == True
                    and password.isdigit() != True and password.isalpha() != True):
                break
            else:
                print('Некорректный пароль!')

        while True:
            password_confirmed = input('Подтвердите пароль: ')
            if password == password_confirmed:
                break
            else:
                print('Пароли не совпадают!')

        return username, password

# Проверка для отладки программы состоящей из нескольких модулей.
if __name__ == '__main__':
    database = DataBase()
    while True:
        choice = input('Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n3 - Для выхода из программы\n')
        # password := - это "моржовый" оператор, работающий внутри функций и запросов как параметр.
        # user = User(input('Введите логин: '), password := input('Введите пароль: '),
        #               password2 := input('Подтвердите пароль: '))
        # if password != password2:
        # exit() - это выход из программы или её завершение.
        #     exit()
        if choice == '1':
            while True:
                username = input('Введите логин: ')
                if username in database.data:
                    password = input('Введите пароль: ')
                    if database.data[username] == password:
                        print('Добро пожаловать,', username)
                        break
                    else:
                        print('Неправильный пароль!')
                else:
                    print('Такого пользователя не найдено!')
        elif choice == '2':
            new_user = User()
            new_user.username, new_user.password = new_user.create_user()
            database.add_user_to_database(new_user.username, new_user.password)
            print(database.data)
        elif choice == '3':
            exit()

# print(User.__doc__)
