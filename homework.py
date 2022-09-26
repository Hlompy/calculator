import datetime as dt


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        day_stats = []
        today = dt.date.today()
        for record in self.records:
            if record.date == today:
                day_stats.append(record.amount)
                total_day_stats = sum(day_stats)
        return total_day_stats

    def get_week_stats(self):
        week_stats = []
        today = dt.date.today()
        seven_days = today - dt.timedelta(days=7)
        for record in self.records:
            if seven_days <= record.date <= today:
                week_stats.append(record.amount)
                total_week_stats = sum(week_stats)
        return total_week_stats

    def remained_money(self):
        remained_money = self.limit - self.get_today_stats()
        return remained_money


class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class CashCalculator(Calculator):
    USD_RATE = 70.0
    EURO_RATE = 77.0
    RUB_RATE = 1

    def get_today_cash_remained(self, currency='rub'):
        currencies = {'usd': ('USD', CashCalculator.USD_RATE),
                      'eur': ('Euro', CashCalculator.EURO_RATE),
                      'rub': ('руб', CashCalculator.RUB_RATE)}
        cash_remained = self.remained_money()

        if cash_remained == 0:
            return 'Денег нет, держись'

        name, meaning = currencies[currency]
        cash_remained = round(cash_remained / meaning, 2)

        if cash_remained > 0:
            return f'На сегодня осталось {cash_remained} {name}'
        if currency not in currencies:
            return 'Данная валюта не поддерживается'

        cash_remained = abs(cash_remained)
        return(f'Денег нет, держись: твой долг - {cash_remained} '
               f'{name}')


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_remained = self.remained_money()
        if calories_remained > 0:
            return ('Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {calories_remained} кКал')
        return'Хватит есть!'
