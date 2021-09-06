class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = list()

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
    return  # should return a string that is a bar chart.
    # The chart should show the percentage spent in each category passed in to the function.
    # The percentage spent should be calculated only with withdrawals and not with deposits.
    # Down the left side of the chart should be labels 0 - 100. 
    # The "bars" in the bar chart should be made out of the "o" character. 
    # The height of each bar should be rounded down to the nearest 10. 
    # The horizontal line below the bars should go two spaces past the final bar. 
    # Each category name should be written vertically below the bar. 
    # There should be a title at the top that says "Percentage spent by category".
    # This function will be tested with up to four categories.

# Testing
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance()) # 973.96
# print(food.ledger)
clothing = Category("Clothing")
food.transfer(50, clothing)
# print(food.get_balance()) # 923.96
# print(clothing.get_balance()) # 50
# print(food.ledger)
# print(clothing.ledger)
clothing.withdraw(25.55) 
# print(clothing.get_balance()) # 24.45
clothing.withdraw(100)
# print(clothing.get_balance()) # 24.45
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
# print(auto.get_balance()) # 985
print(food)
print(clothing)

# print(create_spend_chart([food, clothing, auto]))