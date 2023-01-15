PYBANK, MAIN_PANEL, MANAGE_ACCOUNT = 0, 1, 2
BANK_STUFF, CHARTS, DATAFRAME = 3, 4, 5
GOOD_BYE, NEW_ACCOUNT, MODIFY_ACCOUNT = 6, 7, 8
DEPOSIT, WITHDRAW, INVALID_INPUT = 9, 10, 11
ACC_CREATED, ACC_ALREADY_MODIFIED, ACC_MODIFIED = 12, 13, 14
ARE_SURE, NO_MONEY, BALANCE_CHART = 15, 16, 17
OPERATIONS_CHART, DF_EXPORTED, NO_DEPOSIT = 18, 19, 20
__MARKER_LEN = len('||')


# MSG ------------------------------------------------------------
def get_msg(index):
    msg = ''

    match(index):
        case 0:
            msg = '+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n' \
                + '- PY__BANK, by ~~~~~~~~~~~~~ -\n' \
                + '+ ~~~~~~~~~~~~ David Santana +\n' \
                + '+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-'
        case 1:
            msg = '|----------------------|\n' \
                + '|    .: PY__BANK :.    |\n' \
                + '|----------------------|\n' \
                + '| > [1] Manage Account |\n' \
                + '| > [2] Bank $tuff     |\n' \
                + '| > [3] Charts         |\n' \
                + '| > [4] Dataframe      |\n' \
                + '| > [0] End App.       |\n' \
                + '|----------------------|'
        case 2:
            msg = '|-----------------------|\n' \
                + '| .: MANAGE__ACCOUNT :. |\n' \
                + '|-----------------------|\n' \
                + '| > [1] Show Account    |\n' \
                + '| > [2] Modify Account  |\n' \
                + '| > [3] Way Back        |\n' \
                + '|-----------------------|'
        case 3:
            msg = '|-------------------|\n' \
                + '| .: BANK__$TUFF :. |\n' \
                + '|-------------------|\n' \
                + '| > [1] Balance     |\n' \
                + '| > [2] Deposit     |\n' \
                + '| > [3] Withdraw    |\n' \
                + '| > [4] Way Back    |\n' \
                + '|-------------------|'
        case 4:
            msg = '|------------------------|\n' \
                + '|      .: CHARTS :.      |\n' \
                + '|------------------------|\n' \
                + '| > [1] Balance Chart    |\n' \
                + '| > [2] Operations Chart |\n' \
                + '| > [3] Way Back         |\n' \
                + '|------------------------|'
        case 5:
            msg = '|-----------------------|\n' \
                + '|   .: DATA__FRAME :.   |\n' \
                + '|-----------------------|\n' \
                + '| > [1] Show Dataframe  |\n' \
                + '| > [2] Export .XSLX    |\n' \
                + '| > [3] Export .CSV     |\n' \
                + '| > [4] Way Back        |\n' \
                + '|-----------------------|'
        case 6:
            msg = '+-+-+-+-+-+-\n' \
                + '+ GOOD BYE -\n' \
                + '+-+-+-+-+-+-'
        case 7:
            msg = '| .: NEW__ACCOUNT :. |'
        case 8:
            msg = '| .: MODIFY__ACCOUNT :. |'
        case 9:
            msg = '| .: DEPOSIT :. |'
        case 10:
            msg = '| .: WITHDRAW :. |'
        case 11:
            msg = '| INVALID INPUT! |'
        case 12:
            msg = '| ACCOUNT CREATED! |'
        case 13:
            msg = '| YOUR ACCOUNT ALREADY BEEN MODIFIED! |'
        case 14:
            msg = '| ACCOUNT MODIFIED SUCCESSFULLY! |'
        case 15:
            msg = '| ARE YOU SURE? |'
        case 16:
            msg = '| YOU DONT HAVE MONEY TO WITHDRAW! |'
        case 17:
            msg = '| SHOWING BALANCE CHART... |'
        case 18:
            msg = '| SHOWING OPERATIONS CHART... |'
        case 19:
            msg = '| DATAFRAME EXPORTED! |'
        case 20:
            msg = '| THE ACCOUNT HAS NO DEPOSIT HISTORY! |'
    if (index < 7):
        return msg
    else:
        hyphens = ('-' * (len(msg) - __MARKER_LEN))
        return ('|{0}|\n{1}\n|{2}|'.format(hyphens, msg, hyphens))
# ----------------------------------------------------------------


# FORMAT -------------------------------------------------------------
def f_msg(msg: str):
    msg = msg.splitlines()
    formatted_msg = ''
    larger_line = len(msg[0])

    idx = 1
    while (idx < len(msg)):
        if (larger_line < len(msg[idx])):
            larger_line = len(msg[idx])
        idx += 1

    for idx in range(len(msg)):
        blank_space = ' ' * (larger_line - len(msg[idx]))
        formatted_msg += '| {0}{1} |'.format(msg[idx], blank_space)

        if (idx < (len(msg) - 1)):
            formatted_msg += '\n'

    hyphens = ('-' * (larger_line + __MARKER_LEN))
    return '|{0}|\n{1}\n|{2}|'.format(hyphens, formatted_msg, hyphens)


def f_value(value):
    return format(value, ',.2f')
# --------------------------------------------------------------------


# VALIDATE -------------------------
def validate_name(name: str):
    for letter in name:
        if (not letter.isalpha()):
            return False

    return True


def validate_document(document: str):
    for number in document:
        if (not number.isnumeric()):
            return False

    return True
# ----------------------------------
