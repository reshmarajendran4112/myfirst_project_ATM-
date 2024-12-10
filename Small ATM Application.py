class Bank(object):
    def __init__(self):
        self.closingBal = 0

    def display(self):
        print("Enter your options")
        print("1 for deposit: \n2 for withdraw : ")
        getOption = input()

        if getOption == "1":
            self.deposit()
        elif getOption == "2":
            self.withdraw()
        elif getOption != 1 or getOption != 2:
            print("Thanks")
            return

        print("Your closing balance is : ", self.closingBal)
        print("Do you want to continue : ")
        a = input()
        if a == "Y" or a == "y":
            self.display()
        else:
            print("Thanks for visiting our bank")

    def deposit(self):
        depositAmount = int(input("Enter your deposit amount : "))
        self.closingBal = self.closingBal + depositAmount
        return self.closingBal

    def withdraw(self):
        withdrawAmount = int(input("Enter your withdraw amount : "))
        if self.closingBal >= withdrawAmount:
            self.closingBal = self.closingBal - withdrawAmount
            print("After withdraw your balance amount is : ", self.closingBal)
        else:
            print("No sufficient balance in your account to withdraw")
        return self.closingBal

bankObj = Bank()
bankObj.display()

