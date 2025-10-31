#Create a BankAcct Class that contains at least the following state information: name, account number, amount and interest rate.
#In addition to an __init__ method, the class should support methods for adjusting the interest rate, for withdrawing and
#depositing, and for giving a balance. You should also include a method to calculate the interest based on the number of days.
#Use the __str__ method to display balances and interest amounts. Create a test function to test the different methods in the BankAcct Class.
#The class and test function should be in one .py file.

#This gets the bank account name, number, amount, and interest rate
class BankAcct:
    def __init__(self, name, account_number, amount=0.0, interest_rate=0.01):
        """Initialize a new bank account."""
        self.name = name
        self.account_number = account_number
        self.amount = float(amount)
        self.interest_rate = float(interest_rate)

#Deposit for the bank account
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.amount += amount
            print(f"Deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

#Withdraw for the bank account
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > self.amount:
            print("Insufficient funds for this withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.amount -= amount
            print(f"Withdrew ${amount:.2f}")

#Adjusting the interest rate for the bank account
    def adjust_interest_rate(self, new_rate):
        """Adjust the account's interest rate."""
        if new_rate < 0:
            print("Interest rate cannot be negative.")
        else:
            self.interest_rate = new_rate
            print(f"Interest rate adjusted to {self.interest_rate * 100:.2f}%")

#Calculating the interest for the bank account
    def calculate_interest(self, days):
        """Calculate interest earned over a given number of days."""
        if days < 0:
            print("Number of days cannot be negative.")
            return 0.0
        daily_rate = self.interest_rate / 365
        interest = self.amount * daily_rate * days
        return interest

#Gets the balance for the bank account
    def get_balance(self):
        """Return the current balance."""
        return self.amount

#Returns details for bank account
    def __str__(self):
        """Return account details as a string."""
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate * 100:.2f}%")



#Test function for the program
def test_bank_acct():
    """Test the BankAcct class methods."""
    print("Creating the account...")
    acct = BankAcct("Sonic Hedgehog", "0623199169", 100000000.00, 0.05)

    print("\nInitial Account Info:")
    print(acct)

    print("\nDepositing $500...")
    acct.deposit(500)

    print("\nWithdrawing $200...")
    acct.withdraw(200)

    print("\nAdjusting the interest rate to 6%...")
    acct.adjust_interest_rate(0.06)

    print("\nCalculating interest for 30 days...")
    interest_30_days = acct.calculate_interest(30)
    print(f"Interest for 30 days: ${interest_30_days:.2f}")

    print("\nFinal Account Info:")
    print(acct)

#Run test when script is done
if __name__ == "__main__":
    test_bank_acct()
