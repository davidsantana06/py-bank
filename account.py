from os import system
from person import Person
from threading import Thread
import time as time


class Account:
    BALANCE, DEPOSIT, WITHDRAW = 0, 1, 2
    __GROW_RATE, __SLEEP_TIME = 0.005, 60

    def __init__(self, number, person: Person):
        self.__number = number

        self.__person = person
        self.__modified = False

        self.__first_deposit = True

        self.__balance = 0.0
        self.__growing = False

        self.__history = ([], [], [])  # balance, deposit, withdraw

        self.__thread = Thread(target=self.__update)

    # NUMBER ---------------
    def get_number(self):
        return self.__number
    # ----------------------

    # PERSON ----------------------------
    def set_person(self, person: Person):
        self.__person = person
        self.__modified = True

    def modified(self):
        return self.__modified
    # -----------------------------------

    # DEPOSIT & WITHDRAW ------------------------------
    def first_deposit(self):
        return self.__first_deposit

    def deposit(self, value):
        self.__balance += value
        self.__update_history(self.DEPOSIT, value)
        if (self.__first_deposit):
            self.__start_thread()

    def withdraw(self, value):
        if ((self.__balance - value) >= 0.0):
            self.__balance -= value
            self.__update_history(self.WITHDRAW, value)

            if (self.__balance == 0.0):
                self.__growing = False

            return True
        else:
            return False
    # -------------------------------------------------

    # BALANCE & GROW ------------------------------------------------
    def get_balance(self):
        return self.__balance

    def __update(self):
        while (not self.__first_deposit):
            self.__update_history(self.BALANCE, self.__balance)
            time.sleep(self.__SLEEP_TIME)

            if (self.__growing):
                self.__balance += (self.__balance * self.__GROW_RATE)
    # ---------------------------------------------------------------

    # HISTORY -------------------------------------------------
    def get_history(self):
        return self.__history

    def __update_history(self, idx, value):
        self.__history[idx].append(value)
    # ---------------------------------------------------------

    # THREADS --------------------------
    def __start_thread(self):
        self.__growing = True
        self.__first_deposit = False
        self.__thread.start()

    def stop_thread(self):
        self.__first_deposit = True
        self.__growing = False
    # ----------------------------------

    def __str__(self):
        string = '> Account Number: {0}\n{1}'.format(self.__number, self.__person)

        return string
