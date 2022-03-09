

class User:
    def __init__(self, name , email, balance):
        self.name = name
        self.email = email
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawel(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(self.balance)
        return self


Kanye = User("Kanye", "kanyewest@gmail.com", 1000)
Eminem = User("Eminem", "eminem@gmail.com", 800)
SwaeLee = User("SwaeLee", "swaelee@gmail.com", 500)

Kanye.make_deposit(200)
Kanye.make_deposit(600)
Kanye.make_deposit(400)
Kanye.make_withdrawel(300)
Kanye.display_user_balance()

Eminem.make_deposit(200)
Eminem.make_deposit(300)
Eminem.make_withdrawel(500)
Eminem.make_withdrawel(55)
Eminem.display_user_balance()

SwaeLee.make_deposit(140000)
SwaeLee.make_withdrawel(20)
SwaeLee.make_withdrawel(500)
SwaeLee.make_withdrawel(4500)
SwaeLee.display_user_balance()
