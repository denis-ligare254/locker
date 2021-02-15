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

          print("create password")
          password_created = input()

          print("confirm password")
          password_confirmed = input()
# confirming if the password entered was right
          while password_created != password_confirmed:
              print('wrong password created')
              print('re-enter your password please')
              password_reentered = input()
              print("confirm your password")
 


