import csv
import random
import sqlite3


class MobileCallsQuery:
    """Создание таблиц"""

    @staticmethod
    def create_table():
        with sqlite3.connect('mobile_calls.db') as db:
            cur = db.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS mobile_users(
                UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                User VARCHAR(255) NOT NULL,
                Balance INTEGER NOT NULL);""")
            print('Создание таблицы mobile_users')

            cur.execute("""CREATE TABLE IF NOT EXISTS mobile_price(
                            PriceID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Mts_Mts INTEGER NOT NULL,
                            Mts_Tele2 INTEGER NOT NULL,
                            Mts_Yota INTEGER NOT NULL);""")
            print('Создание таблицы mobile_price')
            db.commit()

    """Создание пользователя"""

    @staticmethod
    def insert_users(data_users):
        with sqlite3.connect('mobile_calls.db') as db:
            cur = db.cursor()

            cur.execute("""INSERT INTO mobile_users (User, Balance) VALUES(?, ?);""", data_users)
            print('Создание нового пользователя')
            db.commit()

    """Установка цен"""

    @staticmethod
    def insert_operators(data_operators):
        with sqlite3.connect('mobile_calls.db') as db:
            cur = db.cursor()

            cur.execute("""INSERT INTO mobile_price (Mts_Mts, Mts_Tele2, Mts_Yota) VALUES(?, ?, ?);""", data_operators)
            print('Установка цен')
            db.commit()

    """Ежедневное списание средств"""

    @staticmethod
    def mouth_call():

        for data in range(1, 31):

            with sqlite3.connect('mobile_calls.db') as db:
                cur = db.cursor()

                cur.execute("""SELECT * FROM mobile_price;""")
                data_info = cur.fetchone()
                data_operator = data_info[0:]

                operator = random.choice(data_operator)
                count_min = random.randrange(1, 11)

                if operator == 1:
                    mobile_operator = 'Mts_Mts'
                elif operator == 2:
                    mobile_operator = 'Mts_Tele2'
                elif operator == 3:
                    mobile_operator = 'Mts_Yota'

                amount = int(operator) * int(count_min)

                cur.execute("""SELECT Balance FROM mobile_users""")
                data_balance = cur.fetchone()
                user_balance = data_balance[0]

                if int(user_balance) < int(amount) or int(user_balance) == 0:
                    print('Недостаточно средств')
                    break

                else:
                    cur.execute(f"""UPDATE mobile_users SET Balance=Balance-{amount} WHERE User='User';""")
                    db.commit()
                    MobileCallsQuery.report_operation(data, mobile_operator, count_min, amount)

    print('Выполнение операции остановлено')

    """Репорт после успешного выполнения операции"""

    @staticmethod
    def report_operation(data, operator, count_min, amount):

        call_report = [
            data, operator, count_min, amount
        ]

        with open('report_mobile.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                call_report
            )
