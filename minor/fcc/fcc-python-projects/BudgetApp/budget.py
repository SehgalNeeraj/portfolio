import math


class Category:
    """[base level class to create Category objects]

    Returns:
        [none]: [returns nothing]
    """

    def __init__(self, budgetCat):
        """[constructs and initializes the object]

        Args:
            budgetCat ([string]): [name of the budget category]
        """
        self.budget_category = budgetCat
        self.balance = 0
        self.ledger = []
        self.withdraw_per_category = 0.0

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
        self.withdraw_per_category += amount

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


def printCategoryNames(categories):
    """[summary]

    Args:
        categories ([type]): [description]
    """

    # find max length of category Name
    max_length = 0
    for category in categories:
        if (len(category.budget_category) > max_length):
            max_length = len(category.budget_category)

    response = ""
    for index in range(max_length):
        cat_str = "     "
        for category in categories:
            try:
                cat_str += (category.budget_category[index]+"  ")
            except:
                cat_str += "   "
                pass
        response += cat_str+"\n"

    # remove last "\n"
    return response[:-1]


def calculatePercentSpend(categories):
    """[summary]

    Args:
        categories ([type]): [description]
    """
    total_spend = 0.0
    percent_spend_per_category = dict()
    for category in categories:
        total_spend += category.withdraw_per_category

    for category in categories:
        percent_spend_per_category[category.budget_category] = int(
            math.floor(10*category.withdraw_per_category/total_spend)*10)

    return percent_spend_per_category


def create_spend_chart(categories):
    """[create bar chart for spending in categories]

    Args:
        categories ([list]): [category list]

    Returns:
        [string]: [bar chart (spending) representation]
    """
    # ! IMP: Print Bar Chart horizontally (line by line) with all data
    percent_spend_per_category = calculatePercentSpend(categories)

    header = "Percentage spent by category\n"
    spend_data = ""

    for i in range(100, -10, -10):
        if (i == 0):
            spend_data += " "

        spend_data += str(i)+"| "
        for (k, v) in percent_spend_per_category.items():
            if (i <= v):
                spend_data += "o  "
            else:
                spend_data += "   "
        spend_data += "\n"+" "

    category_str = printCategoryNames(categories)
    horizontal_line = "   "+"-"*(len(categories)*3+1)
    spend_chart = header + spend_data + \
        horizontal_line + "\n" + category_str

    return spend_chart
