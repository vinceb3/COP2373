# The BankAcct class creates a bank account, initialized with the
# account holder's name, the account number, the starting balance, and
# the interest rate. Some of these can be changed with class methods.
class BankAcct:
    # Initialize to starting variables
    def __init__(self, name, acct_num, balance, rate):
        self.__name = name
        self.__acct_num = acct_num
        self.__balance = balance
        self.__rate = rate

    # Change the interest rate to the provided decimal number
    def change_rate(self, rate):
        self.__rate = rate

    # Withdraw the provided amount of money
    def withdraw(self, withdrawal):
        self.__balance -= withdrawal

    # Deposit the provided amount of money
    def deposit(self, deposit):
        self.__balance += deposit

    # Calculates and return the money generated from interest over
    # a number of days (compounded interest).
    def calc_interest(self, days):
        balance_after = (self.__balance * (1 + (self.__rate / 365)) ** days) - self.__balance
        return balance_after

    # Returns a string containing info for the account.
    def __str__(self):
        return(f"\n{self.__name}'s account\n"
               f"Balance: ${self.__balance:,.2f}\n"
               f"Interest rate: {self.__rate:.2%}\n")

def class_test():
    vince_acct = BankAcct("Vince", 3737, 1.20, 0.04)
    print(vince_acct)
    vince_acct.change_rate(0.05)
    vince_acct.withdraw(1)
    vince_acct.deposit(10)
    print(vince_acct)
    print(f"Hypothetical compounded interest over a month: ${vince_acct.calc_interest(30):,.2f}")

def main():
    class_test()

if __name__ == "__main__":
    main()
