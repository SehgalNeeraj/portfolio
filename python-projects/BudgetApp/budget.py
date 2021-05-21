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
        """[summary]

        Args:
            amount ([type]): [description]
            description (str, optional): [description]. Defaults to ''.
        """
        self.balance = self.balance + amount
        depositObj = {f'amount': amount, 'description': description}
        self.ledger.append(depositObj)

    def withdraw(self, amount, description=''):
        """[summary]

        Args:
            amount ([type]): [description]
            description (str, optional): [description]. Defaults to ''.

        Returns:
            [type]: [description]
        """
        if (self.check_funds(amount) is False):
            return False

        self.balance = self.balance - amount
        withdrawObj = {f'amount': (-1 * amount), 'description': description}
        self.ledger.append(withdrawObj)

        return True

    def get_balance(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.balance

    def transfer(self, amount, cat_obj):
        """[summary]

        Args:
            amount ([type]): [description]
            cat_obj ([type]): [description]

        Returns:
            [type]: [description]
        """
        if (self.check_funds(amount) is False):
            return False

        description = f"Transfer to {cat_obj.budget_category}"
        self.withdraw(amount, description)

        description = f"Transfer from {self.budget_category}"
        cat_obj.deposit(amount, description)

        return True

    def check_funds(self, amount):
        """[summary]

        Args:
            amount ([type]): [description]

        Returns:
            [type]: [description]
        """
        if (amount > self.balance):
            return False

        return True

    def __banner(self, numChars=30, decorator="*"):
        """[Returns centrally aligned string of length padded with decorator]

        Args:
            numChars ([integer]): [length of line]
            decorator ([string]): [decorator to pad the string]

        Returns:
            [string]: [centered aligned Category name padded with decorator]
        """
        banner = self.budget_category.center(numChars, decorator)
        return banner

    def __ledger_to_string(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        ledger_items = ""
        for item in self.ledger:
            ledger_items += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
        
        return (ledger_items)

    def __str__(self):
        """[String representation of the Object]

        Returns:
            [string]: [String representation of the Object]
        """
        banner = self.__banner(30, "*")
        ledger_to_string = self.__ledger_to_string()
        category_total = str(self.get_balance())

        objectStr = f"{banner}\n{ledger_to_string}Total: {category_total}"
        return (objectStr)


def create_spend_chart(categories):
    pass
