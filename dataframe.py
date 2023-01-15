import pandas as pd
import text_pattern as tp


class Dataframe:
    XLSX, CSV = 2, 3

    def __init__(self, balance: list):
        self.__balance = balance

    # DAYS COUNTER -------------------------
    def __count_days(self):
        days = []
        for i in range(len(self.__balance)):
            days.append((i + 1))

        return days
    # --------------------------------------

    # AMOUNT & PERCENTAGE CHANGE -------------------------------------------------------------------
    def __changes(self):
        changes = (['-'], ['-'])

        idx = 0
        while (idx < (len(self.__balance) - 1)):
            a_change = self.__balance[idx] - self.__balance[(idx + 1)]
            p_change = (self.__balance[(idx + 1)] - self.__balance[idx]) / self.__balance[idx] * 100
            signal = ''
            if (a_change != 0):
                signal = '+' if (a_change < 0) else '-'

            changes[0].append(signal + tp.f_value(abs(a_change)))
            changes[1].append(signal + tp.f_value(abs(p_change)))

            idx += 1

        return changes
    # ----------------------------------------------------------------------------------------------

    # DATAFRAME -------------------------------------------------
    def __make_df(self):
        balance = [tp.f_value(value) for value in self.__balance]
        changes = self.__changes()

        df_relation = {
            'Day': self.__count_days(),
            'Balance': balance,
            'Amount Change': changes[0],
            '% Change': changes[1]
        }

        return pd.DataFrame(df_relation)

    def get_df(self):
        valid_df = False
        while (not valid_df):
            try:
                df = self.__make_df()
                valid_df = True
            except:
                pass

        return df
    # -----------------------------------------------------------

    # EXPORT ----------------------------------------
    def export_df(self, df: pd.DataFrame, extension):
        if (extension == self.XLSX):
            df.to_excel('py_bank.xlsx', index=False)
        elif (extension == self.CSV):
            df.to_csv('py_bank.csv', index=False)
    # -----------------------------------------------
