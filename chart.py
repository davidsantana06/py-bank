from account import Account
import matplotlib.pyplot as plt


class Chart:
    PLOT, BAR = 1, 2

    def __init__(self, history: tuple, model):
        self.__history = history
        self.__model = model

    # DAYS COUNTER ------------------------------------------
    def __count_days(self):
        days = []
        for i in range(len(self.__history[Account.BALANCE])):
            days.append('Day {0}'.format(i + 1))

        return days
    # -------------------------------------------------------

    # CHART --------------------------------------------------------------
    def __make_chart(self):
        chart = plt

        if (self.__model == self.PLOT):
            chart_data = {'days': self.__count_days(),
                          'balance': self.__history[Account.BALANCE]}

            chart.plot(chart_data['days'],
                       chart_data['balance'],
                       label='Value ($)',
                       marker='o',
                       color='#0D214F')

            chart.grid(True, linestyle='--')
            chart.legend()
        elif (self.__model == self.BAR):
            chart_data = {'operations': ['Deposit', 'Withdraw'],
                          'op_times': [len(self.__history[Account.DEPOSIT]),
                                       len(self.__history[Account.WITHDRAW])]}

            chart.bar(chart_data['operations'],
                      chart_data['op_times'],
                      align='center',
                      alpha=0.5,
                      color=['#0D214F', '#DC493A'])

            chart.xlabel('Operation')
            chart.ylabel('Times')

        chart.title('Bank History', fontsize=13)

        return chart

    def show_chart(self):
        valid_chart = False
        while not (valid_chart):
            try:
                chart = self.__make_chart()
                valid_chart = True
            except:
                pass

        chart.show()
    # --------------------------------------------------------------------
