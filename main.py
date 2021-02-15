#  provides access to functions that support these types of operations
import random
# importing user class form login file
from login import User_login

# main function 
def main():
    while True:
       print("welcome to password locker")
       print("\n")
       print("what do you want to do?")
# created a dummy variable that holds any inputs that the user will choose
       detail_holder = input()
      
       print("\n")
       if detail_holder == "sign-in":
          print('create username')
          username_created = input()


