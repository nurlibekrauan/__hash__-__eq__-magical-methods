class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

    def validate_email(self, email):
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email address")

    def validate_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.validate_name(value)
        self.__name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.validate_email(value)
        self.__email = value

    def __eq__(self, other):
        return self.email == other.email

    def __hash__(self):
        return hash(self.email)


user1 = User("user1", "email@example.com")
user2 = User("user2", "email@example.com")
user3 = User("user3", "another@example.com")

# Сравнение пользователей
print(user1 == user2)  # True
print(user1 == user3)  # False

# Использование в множестве
user_set = {user1, user2, user3}
print(len(user_set))  # 2, т.к. user1 и user2 считаются одинаковыми
