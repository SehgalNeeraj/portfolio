class Category:
    budget_category = ""
    ledger_list = []
    balance = 0

    def __init__(self, budgetCat):
        self.budget_category = budgetCat
        self.balance = 0

    def deposit(self, amount, description=""):
        self.balance = self.balance + amount
        depositObj = '{"amount":{amount},"description":{description}}'
        self.ledger_list.append(depositObj)

    def withdraw(self, amount, description=""):
        if (self.check_funds(amount) is False):
            return False

        self.balance = self.balance - amount
        withdrawObj = '{"amount":{-1 * amount},"description":{description}}'
        self.ledger_list.append(withdrawObj)

        return True

    def get_balance(self):
        return self.balance

    def transfer(self,amount,cat_obj):
        pass

    def check_funds(self, amount):
        if (amount > self.balance):
            return False

        return True

def create_spend_chart(categories):
    pass
