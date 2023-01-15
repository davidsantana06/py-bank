from account import Account
from chart import Chart
from dataframe import Dataframe
from datetime import datetime
from person import Person
from random import randint
import re as re
import sys as sys
import text_pattern as tp
import time as time


# AUX METHODS -----------------------------------------------------------------------
def __print(msg):
    print('\n' + msg)


def __clear_terminal():
    print('\n' * 6)

    for char in '... cleaning ...':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.09)

    print('\n' * 6)


def __data_input(text, type):
    valid_input = False
    while (not valid_input):
        data = input('_{0}: '.format(text))

        if (type == 'name'):
            valid_input = tp.validate_name(data)
        elif (type == 'doc'):
            valid_input = tp.validate_document(data)
        else:
            try:
                data = datetime.strptime(data, str(Person.DATE_FORMAT))
                valid_input = True
            except:
                pass
        
        if (not valid_input):
            __print(tp.get_msg(tp.INVALID_INPUT))

    return data


def __account_data():
    data = {0: __data_input('First Name', 'name'),
            1: __data_input('Last Name', 'name'),
            2: __data_input('Document', 'doc'),
            3: __data_input('Birtdate', 'birthdate')}

    return data


def __value_input():
    valid_value = False
    while (not valid_value):
        try:
            value = float(input('_Value: '))
            if (value > 0):
                valid_value = True
            else:
                result = 'THE VALUE {0} IS INVALID!'.f(value)
                __print(tp.f_msg(result))
        except:
            __print(tp.get_msg(tp.INVALID_INPUT))

    return value


def __valid_operation(first_op, last_op, operation):
    return (len(operation) == 1 and (operation >= first_op and operation <= last_op))
# -----------------------------------------------------------------------------------

# ACCOUNT ---------------------------------------------------------
def new_account():
    __print(tp.get_msg(tp.NEW_ACCOUNT))
    data = __account_data()
    person = Person((data[0] + ' ' + data[1]), data[2], data[3])
    number = '{0}-{1}'.format(randint(100,1000), randint(100,1000))
    account = Account(number, person)
    __print(tp.get_msg(tp.ACC_CREATED))

    return account


def modify_account(account: Account):
    __print(tp.get_msg(tp.MODIFY_ACCOUNT))
    data = __account_data()
    person = Person((data[0] + ' ' + data[1]), data[2], data[3])
    account.set_person(person)
    __print(tp.get_msg(tp.ACC_MODIFIED))


def manage_account(account: Account):
    __print(tp.get_msg(tp.MANAGE_ACCOUNT))
    operation = input('_Operation: ')
    if (operation != '3'):
        match (operation):
            case '1':
                __print(tp.f_msg(str(account)))
            case '2':
                if (account.modified()):
                    __print(tp.get_msg(tp.ACC_ALREADY_MODIFIED))
                else:
                    modify_account(account)
            case _:
                __print(tp.get_msg(tp.INVALID_INPUT))
        return True
    else:
        return False
# -----------------------------------------------------------------


# BANK STUFF ------------------------------------------------------------------------
def bank_stuff(account: Account):
    __print(tp.get_msg(tp.BANK_STUFF))
    operation = input('_Operation: ')
    if (operation != '4'):
        match (operation):
            case '1':
                __print(tp.f_msg('Balance: $' + tp.f_value(account.get_balance())))
            case '2':
                __print(tp.get_msg(tp.DEPOSIT))
                value = __value_input()
                account.deposit(value)
                __print(tp.f_msg('$' + tp.f_value(value) + ' deposited!'))
            case '3':
                if (not account.get_balance() == 0.0):
                    __print(tp.get_msg(tp.WITHDRAW))
                    value = __value_input()
                    if (account.withdraw(value)):
                        __print(tp.f_msg('$' + tp.f_value(value) + ' withdrawn!'))
                    else:
                        __print(
                            tp.f_msg('$' + tp.f_value(value) + ' exceed the limit!'))

                else:
                    __print(tp.get_msg(tp.NO_MONEY))
            case _:
                __print(tp.get_msg(tp.INVALID_INPUT))
        return True
    else:
        return False
# -----------------------------------------------------------------------------------


# CHARTS ------------------------------------------------------------------------------------
def charts(account: Account):
    __print(tp.get_msg(tp.CHARTS))
    operation = input('_Operation: ')
    if (operation != '3'):
        match (operation):
            case '1' | '2':
                if (not account.first_deposit()):
                    msg_idx = tp.BALANCE_CHART if (operation == '1') else tp.OPERATIONS_CHART
                    __print(tp.get_msg(msg_idx))

                    chart = Chart(account.get_history(), (int(operation))) 
                    chart.show_chart()
                else:
                    __print(tp.get_msg(tp.NO_DEPOSIT))
            case _:
                __print(tp.get_msg(tp.INVALID_INPUT))
        return True
    else:
        return False
# -------------------------------------------------------------------------------------------


# DATAFRAME ----------------------------------------------------------
def data_frame(account: Account):
    __print(tp.get_msg(tp.DATAFRAME))
    operation = input('_Operation: ')
    if (operation != '4'):
        if (not account.first_deposit()):
            if (__valid_operation('1', '3', operation)):
                df = Dataframe(account.get_history()[Account.BALANCE])

                if (operation == '1'):
                    __print(tp.f_msg(str(df.get_df())))
                else:
                    df.export_df(df.get_df(), int(operation))
                    __print(tp.get_msg(tp.DF_EXPORTED))
            else:
                __print(tp.get_msg(tp.INVALID_INPUT))
        else:
            __print(tp.get_msg(tp.NO_DEPOSIT))
        return True
    else:
        return False
# --------------------------------------------------------------------


# MAIN --------------------------------------------------
def main():
    print(tp.get_msg(tp.PYBANK))
    account = new_account()
    __clear_terminal()

    end_app = False
    while (not end_app):
        __print(tp.get_msg(tp.MAIN_PANEL))
        operation = input('_Operation: ')

        if (operation == '0'):
            account.stop_thread()
            end_app = True
            __print(tp.get_msg(tp.GOOD_BYE))
        elif (__valid_operation('1', '4', operation)):
            __clear_terminal()

            match (operation):
                case '1':
                    while (True):
                        if (not manage_account(account)):
                            break
                case '2':
                    while (True):
                        if (not bank_stuff(account)):
                            break
                case '3':
                    while (True):
                        if (not charts(account)):
                            break
                case '4':
                    while (True):
                        if (not data_frame(account)):
                            break

            __clear_terminal()
        else:
            __print(tp.get_msg(tp.INVALID_INPUT))
# -------------------------------------------------------


main()
