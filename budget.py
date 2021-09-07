class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description = ''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({"amount": amount * -1, "description": description})
            return True

        return False

    def get_balance(self): 
        balance = 0
        for entry in self.ledger:
            balance += entry['amount']

        return balance

    def transfer(self, amount, target_category):
        if self.check_funds(amount):
            self.ledger.append({"amount": amount * -1, "description": f"Transfer to {target_category.category}"})
            target_category.deposit(amount, f"Transfer from {self.category}")
            return True

        return False

    def check_funds(self, amount):
        balance = self.get_balance()
        return False if amount > balance else True

    def __str__(self):
        print_str = f"{self.category:*^30}"

        for entry in self.ledger: 
            print_str += f"\n{entry['description']:<23.23}"
            print_str += f"{entry['amount']:>7.2f}"

        print_str += f"\nTotal: {self.get_balance()}"

        return print_str

def create_spend_chart(categories):
    
    category_names = []
    withdrawals = []

    for category in categories:
        category_names.append(category.category)
        debits = [
            abs(line['amount']) 
            for line in category.ledger 
            if line['amount'] < 0
        ]
        withdrawals.append(sum(debits))

    percent_spending = [
        (int(amt / sum(withdrawals) * 100 * (10**-1)) * 10) 
        for amt in withdrawals
    ]

    # Construct chart
    chart_lines = 12
    max_cat_name_length = max([len(name) for name in category_names])
    chart = 'Percentage spent by category\n'

    for i in range(chart_lines + max_cat_name_length):
        percent = (10 - i) * 10

        # Construct chart body
        if percent >= 0:
            # Set vertical percent label
            chart += f'{percent:>3}|'

            # Set data mark on chart or empty space
            for i in range(len(percent_spending)):
                mark = ' o ' if percent_spending[i] >= percent else '   '
                chart += mark
            chart += ' \n'

        # Set bottom line of chart
        elif percent == -10:
            chart += '    '
            for i in range(len(percent_spending)):
                if i < len(percent_spending) - 1:
                    mark = '---'
                else: 
                    mark = '----'
                chart += mark
            chart += '\n'

        # Construct bottom labels
        else:
            chart += '    '
            index = i - chart_lines
            for name in category_names:
                if index < len(name):
                    chart += f' {name[index]} '
                else: 
                    chart += '   '

            if index < max_cat_name_length - 1:
                chart += ' \n'
            else: 
                chart += ' '

    return chart
