from threading import Thread, Lock

lock = Lock()


class BankAccount(Thread):

    def __init__(self, amount=1000):
        super().__init__()
        self.amount = amount

    def deposit(self, new_amount):
        with lock:
            self.amount += new_amount
            print(f'Deposited {new_amount}, new balance is {self.amount}')

    def withdraw(self, new_amount):
        with lock:
            self.amount -= new_amount
            print(f'Withdrew  {new_amount}, new balance is {self.amount}')


def deposit_task(bank_account, amount):
    for _ in range(5):
        bank_account.deposit(amount)


def withdraw_task(bank_account, amount):
    for _ in range(5):
        bank_account.withdraw(amount)


account = BankAccount()

deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()


