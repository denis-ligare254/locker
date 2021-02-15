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
          secret_created = input()

          print("confirm secret-key")
          secret_confirmed = input()
# confirming if the password entered was right
          while secret_created != secret_confirmed:
              print('invalid key entered')
              print('re-enter your secret-key')
              secret_created = input()
              print("confirm your secret-key")
              secret_confirmed = input()
 # if the code details entered was okay,the following code will run
          else:
                print("congrats,account created")
                print("\n")
                print("log your credentials")
                print("enter username")
                username =input()
                print("enter secret-key")
                secretkey = input()
          while username !=username_created or secret_created != secretkey:
                print('invalid details')
                print('')
                
                


