#  provides access to functions that support these types of operations
import random
# importing user class form login file
from login import logins

# main function 
def main():
    while True:
       print("welcome to password locker")
       print("\n")
       print("what do you want to do?create account,sign in or exit?type your answer below")
# created a dummy variable that holds any inputs that the user will choose
       detail_holder = input()
      
       print("\n")
       if detail_holder == "sign-in":
          print('enter username')
          username_created = input()

          print("create secret-key")
          password_created = input()

          print("confirm secret-key")
          password_confirmed = input()
# confirming if the password entered was right
          while password_created != password_confirmed:
              print('invalid key entered')
              print('re-enter your password please')
              password_reentered = input()
              print("confirm your password")
 # if the code details entered was okay,the following code will run
          else:
                print("congrats,account created")
                print("\n")
                print("log your credentials")
                password =input()
                
                


