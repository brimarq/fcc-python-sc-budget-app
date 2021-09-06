class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = list()

    def deposit(self, amount, description = ''):
        # should append an object to the ledger list in the form of {"amount": amount, "description": description}.
        return

    def withdraw(self, amount, description = ''):
        # amount passed in should be stored in the ledger as a negative number.
        #  If there are not enough funds, nothing should be added to the ledger. 
        return # This method should return True if the withdrawal took place, and False otherwise.

    def get_balance(self): 
        return  # returns the current balance of the budget category based on the deposits and withdrawals that have occurred.

    def transfer(self, amount, category):
        # should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
        # should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]" 
        # If there are not enough funds, nothing should be added to either ledgers. 
        return # This method should return True if the transfer took place, and False otherwise.

    def check_funds(self, amount):
        # This method should be used by both the withdraw method and transfer method.
        return  # returns False if the amount is greater than the balance of the budget category and returns True otherwise. 

    def __str__(self):
        # When the budget object is printed it should display:
        # A title line of 30 characters where the name of the category is centered in a line of * characters. 
        # A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters. 
        # A line displaying the category total.
        return 





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

