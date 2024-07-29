# race_condition

import threading
import time

x = 0
# Блокировка
# Блокирует использование части кода для нескольких потоков.
# Только поток, который первый дошёл до начала блокировки будет использовать этот участок кода.
# После выхода из блокировки идёт следующий поток и так далее.
lock = threading.Lock()


def thread_task():
    global x
    for _ in range(10_000_000):
        # Начало блокировки.
        # lock.acquire()
        # x = x + 1
        # Конец блокировки.
        # lock.release()
        # Или с помощью with
        # with lock:
        #    x = x + 1
        x = x + 1

# Атомарные операции - либо выполняются за один тик, либо не выполняется вообще.
# Это же неатомарная операция, то есть операция состоящая из нескольких действий.
# Каждый поток делает следующие действия:
# 1. Считывает значение x | x = 0
# 2. Производит вычисления нового значения x | x = 0 + 1
# 3. Записывает новое значение x | x = 1
# Во время неатомарных действий потоки могут перезаписать операцию друг друга, так как начнут действие до того,
# как другой поток успеет закончить эту же самую операцию.
# Но начиная с версии python3.10 эта операция является атомарной.


def main():
    global x
    x = 0

    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


for i in range(10):
    main()
    print(x)

# Взаимно заблокированные потоки.
# Когда один блок блокирует доступ для потока, который должен снять блокировку.
# Но на новых версиях python этот пример тоже уже нормально работает.
lock1 = threading.Lock()
lock2 = threading.Lock()


def thread_task1():
    lock1.acquire()
    print('thread 1 lock1 acquired')
    time.sleep(1)
    lock2.acquire()
    print('thread 1 lock2 acquired')
    lock2.release()
    lock1.release()


def thread_task2():
    lock2.acquire()
    print('thread 2 lock2 acquired')
    time.sleep(1)
    lock1.acquire()
    print('thread 2 lock1 acquired')
    lock1.release()
    lock2.release()


thr1 = threading.Thread(target=thread_task1())
thr2 = threading.Thread(target=thread_task2())

thr1.start()
thr2.start()

thr1.join()
thr2.join()
