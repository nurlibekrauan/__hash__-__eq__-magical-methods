class Transaction:
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount

    def validate_transaction_id(self, value):
        if not isinstance(value, str):
            raise ValueError("Transaction ID must be a string")

    def validate_amount(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Amount must be a number")
        if value <= 0:
            raise ValueError("Amount must be positive")

    @property
    def transaction_id(self):
        return self.__transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self.validate_transaction_id(value)
        self.__transaction_id = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.validate_amount(value)
        self.__amount = value

    def __eq__(self, other: "Transaction"):
        return self.transaction_id == other.transaction_id

    def __hash__(self):
        return hash(self.transaction_id)

transaction1 = Transaction("TXN12345", 500)
transaction2 = Transaction("TXN12345", 1000)
transaction3 = Transaction("TXN67890", 750)

# Сравнение транзакций
print(transaction1 == transaction2)  # True
print(transaction1 == transaction3)  # False

# Проверка уникальности транзакций в множестве
transaction_set = {transaction1, transaction2, transaction3}
print(len(transaction_set))  # 2, т.к. transaction1 и transaction2 считаются одинаковыми
