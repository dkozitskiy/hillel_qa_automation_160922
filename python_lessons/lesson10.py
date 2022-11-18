"""
1. Створити клас Банківського рахунку
2. атрибут класу - депозитний портфель
3. клас при ініціалізації отримує імя користувача, початкову суму внеску,
та відсоток нарахування на залишок по рахунку (передається цілим числом, проте є приватним (__ у назві))
4. при ініціалізації також автоматично генерується дата відкриття рахунку та унікальний ідентифікатор рахунку - для цього погляньте як працює
import uuid
print(uuid.uuid4())
5. створити геттер та сеттер для зміни ставки по рахунку (аналог дня дародження на прикладі, описаному на лекції)
6. перевизначте метод __str__ (наповнення - на ваш вибір)
7. створіть методи для поповнення та зняття коштів з рахунку (рахунок не може мати негативний баланс)
8. створіть класметоди для контролю депозитного портфелю (запускаються в ініціалізаторі, методах поповнення та зняття, __del__
9. перевизначте метод __del__ - при його виклику автоматично знімаються всі кошти з рахунків власника
та ПРИНТИТЬСЯ повідомлення, що у такого то власника закрито рахунок у звязку з ліквідацією банка, повернуто таку-то суму,
власник препензій не має (це один із двох принтів в програмі, все інше має бути здано без принтів - при розробці користуйтеся дебагером чи принтами, на ваш вибір)
10. створіть метод трансфер, який дозволяє переводити кошти з одного рахунку на інший
11. створіть метод get_todays_profit, задекорований через property
він має автоматично розраховувати плановий прибуток за сьогоднішній день з огляду на поточний залишок на рахунку
та відсоткову ставку (зауважте, ставка в ініціалізаторі - річна, а за день 1/365 ставки * суму)
12. створіть метод, задекорований staticmethod.
в ньому буде принтом (одним із двох в програмі) виводитися рекламний слоган банку - вигадайте щось помпезне
можете скористатися
https://www.geeksforgeeks.org/art-module-in-python/
https://towardsdatascience.com/rich-generate-rich-and-beautiful-text-in-the-terminal-with-python-541f39abf32e
чи самостійно пошукати аналог
головне памятайте - щось встановлюєте ручками, то кріпите requirements.txt

13. створити мінімум два рахунки
14. в одному з них змінити ставку
15. внести та зняти кошти
16. перевести кошти (чи їх частину) одного рахунку на інший (не дозволяєм заходити в мінуса по рахункам)
17. впевнитися, що виконуються дії, описані в __del__, при закінченні роботи програми
"""

import uuid
from datetime import datetime


class BankAccount:
    """
    Bank deposit class. Accumulation of the bank's loan portfolio and operations with customer deposits are available
    """

    deposit_portfolio = 0

    def __init__(self, user_name: str, initial_amount: int, percent: int):
        self.user_name = user_name
        self.initial_amount = initial_amount
        self.__percent = percent
        self.opening_date = datetime.now().date()
        self.id_deposit = uuid.uuid4()
        self.money = self.initial_amount
        BankAccount.portfolio_increase(self.initial_amount)

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, value: int):
        """Change interest on deposits. Value format must be int and >=0"""
        if type(value) is int and value >= 0:
            self.__percent = value

    def __str__(self):
        return f'user name: {self.user_name}, initial amount: {self.initial_amount}, percent: {self.__percent}, ' \
               f'opening date: {self.opening_date}, id_deposit: {self.id_deposit}, deposit sum: {self.money}'

    def top_up_dep(self, top_up_sum: int):
        """
        deposit replenishment
        top_up_sum format must be int and > 0
        """
        if type(top_up_sum) is int and top_up_sum > 0:
            BankAccount.portfolio_increase(top_up_sum)
            self.money += top_up_sum

    def withdraw_dep(self, withdraw_sum: int):
        """
        withdrawal of money from the deposit
        withdraw_sum format must be int and > 0
        """
        if type(withdraw_sum) is int and 0 < withdraw_sum <= self.money:
            BankAccount.portfolio_reduction(withdraw_sum)
            self.money -= withdraw_sum
        else:
            raise Exception("the amount does not meet the requirements! withdraw_sum format must be int and > 0")

    @classmethod
    def portfolio_increase(cls, summa: int):
        BankAccount.deposit_portfolio += summa

    @classmethod
    def portfolio_reduction(cls, summa: int):
        if BankAccount.deposit_portfolio >= summa:
            BankAccount.deposit_portfolio -= summa
        else:
            raise Exception("the amount exceeds the amount of money in the bank")

    def money_transfer(self, other, summa: int):
        """
        Transferring money from one deposit to another
        :param other: indicate the copy to which you want to transfer
        :param summa: (int) amount to transfer. Integer. The amount cannot be more than what is on the balance of the instance
        """
        if other.money >= summa:
            self.money -= summa
            other.money += summa
        else:
            raise Exception("The amount is more than what is in the account")

    @property
    def get_todays_profit(self):
        """
        returns a value with the client's benefit for one day, taking into account the annual rate
        """
        todays_profit = ((self.__percent / 365) * self.money) / 100
        return todays_profit

    @staticmethod
    def slogan():
        print("Dear Bank Director!\nPlease lower interest rates! The wife brings you all the free money.\nAnd I want a bike!\n")

    def __del__(self):
        BankAccount.portfolio_reduction(self.money)
        print(f'''Deposit ID {self.id_deposit} in the name of {self.user_name} - closed due to the liquidation of the Bank. The amount
{self.money} was returned, the owner has no claims\n''')
        self.money -= self.money


if __name__ == '__main__':
    ivan = BankAccount('Ivan', 5_000, 10)
    egor = BankAccount('Egor', 30_000, 10)
    dazdraperma = BankAccount('Dazdraperma', 10_000, 5)
    dazdraperma.percent = 10
    ivan.top_up_dep(5_000)
    egor.withdraw_dep(20_000)
    dazdraperma.money_transfer(ivan, 5_000)
