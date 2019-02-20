import os
import pickle
import tempfile

class Transaction(object):
    def __init__(self, amount, date, currency="USD", usd_conversation_rate=1, description="None"):
        """
        >>> t = Transaction(100, "2008-12-09")
        >>> t.amount, t.currency, t.usd_conversion_rate, t.usd
        (100, 'USD', 1, 100)
        >>> t = Transaction(250, "2009-03-12", "EUR", 1.53)
        >>> t.amount, t.currency, t.usd_conversion_rate, t.usd
        (250, 'EUR', 1.53, 382.5)
        """
        self.__amount = amount
        self.__date = date
        self.__currency = currency
        self.__usd_conversion_rate = float(usd_conversation_rate)
        self.__description = description
        self.__usd = self.__amount * self.__usd_conversion_rate

    @property
    def amount(self):
        return self.__amount

    @property
    def date(self):
        return self.__date

    @property
    def currency(self):
        return self.__currency

    @property
    def usd_conversion_rate(self):
        return self.__usd_conversion_rate

    @property
    def description(self):
        return self.__description

    @property
    def usd(self):
        return self.__usd

    def __repr__(self):
        return "{0.amount} {0.date} {0.currency} {0.usd_conversion_rate} {0.description} {0.usd}".format(self)


class Account(object):
    def __init__(self, account_number, account_name, transactions=None):
        assert len(account_name) > 4, "length name must be > 4"
        self.__transactions = []
        if transactions is not None:
            self.__transactions.append(transactions)
        self.__account_number = int(account_number)
        self.__account_name = account_name

    @property
    def account_number(self):
        return self.__account_number

    @property
    def transactions(self):
        return self.__transactions

    @property
    def balance(self):
        amount = 0
        for usd in self.__transactions:
            amount += usd.amount
        return amount

    def account_name(self, name=None):
        if name is not None:
            assert len(name) > 4, "length name must be > 4"
            self.__account_name = name
        else:
            return "{}".format(self.__account_name)

    def apply(self, transaction):
        print(type(transaction))
        if type(transaction) == Transaction:
            self.__transactions.append(transaction)
        else:
            raise Exception

    def __repr__(self):
        return "{} {} {}".format(self.__account_number, self.__account_name, self.__transactions)

    def __len__(self):
        return len(self.__transactions)

    def all_usd(self):
        for transaction in self.__transactions:
            if transaction.currency != "USD":
                return False
        return True

    def save(self, filename=None):
        if filename is None:
            name = os.path.join(tempfile.gettempdir(), "{}.acc".format(self.__account_name))
        elif filename.lower().endswith(".acc"):
            name = os.path.join(tempfile.gettempdir(), filename)
        file = open(name, "wb")
        pickle.dump(self, file, pickle.HIGHEST_PROTOCOL)
        print(name)
        if file is not None:
            file.close()

    @staticmethod
    def load(filename):
        file = open(os.path.join(tempfile.gettempdir(), filename), "rb")
        return pickle.load(file)