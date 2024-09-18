                                    # Encapsulation

# Encapsulation restricts direct access to some of an object's components,
# which means you can control how the internal state is accessed or modified.

# Example: Getters and Setters (Encapsulation)

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance # private variable
#
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Invalid Deposit Amount")
#
#     def withdrawl(self, amount):
#         if amount > 0:
#             self.balance -= amount
#         else:
#             print("Invalid Withdrawl Amount")
#
#     def view_balance(self):
#         return self.balance
#
# hdfc_account = BankAccount(25000)
#
# hdfc_account.deposit(5000)
#
# hdfc_account.withdrawl(15000)
#
# print(hdfc_account.view_balance())
#
# print(BankAccount.balance)

"""
Here, __balance is a private variable, meaning it can't be accessed directly from outside the class. 
Instead, the balance can be accessed and modified only through methods like deposit(), withdraw(), and get_balance(),
thus encapsulating the data.
"""