class Category:
    """[base level class to create Category objects]

    Returns:
        [none]: [returns nothing]
    """
    budget_category = ""
    ledger = []
    balance = 0

    def __init__(self, budgetCat):
        """[constructs and initializes the object]

        Args:
            budgetCat ([string]): [name of the budget category]
        """
        self.budget_category = budgetCat
        self.balance = 0
        self.ledger = []

    def deposit(self, amount, description=''):
        self.balance = self.balance + amount
        depositObj = {f'amount': amount, 'description': description}
        self.ledger.append(depositObj)

    def withdraw(self, amount, description=''):
        if (self.check_funds(amount) is False):
            return False

        self.balance = self.balance - amount
        withdrawObj = {f'amount':(-1 * amount), 'description': description}
        self.ledger.append(withdrawObj)

        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, cat_obj):
        if (self.check_funds(amount) is False):
            return False

        description = f"Transfer to {cat_obj.budget_category}"
        self.withdraw(amount, description)

        description = f"Transfer from {self.budget_category}"
        cat_obj.deposit(amount, description)

        return True

    def check_funds(self, amount):
        if (amount > self.balance):
            return False

        return True

    # def __str__(self):
        printName = '{:*^30}'.format(self.budget_category)

        printItem = ""
        for item in self.ledger:
            desc = item.find("n:")
            amount_start = item.find(":")
            amount_end = item.find(",")
            # printItem = printItem + '{:<23}'.format(item[desc+2:-1][:23]) + \
                # " " + \
                # '{:>-7.2f}'.format(float(item[amount_start+1:amount_end]))+"\n"

        totalStr = "Total: "+str(self.get_balance())
        return (printName+"\n"+"\n"+totalStr)


def create_spend_chart(categories):
    pass
