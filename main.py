#getpass module is used to encrypt password
from  getpass import getpass
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
       if detail_holder == "create account":
          print('enter username')
          username_created = input()

          print("create secret-key")
          secret_created = getpass()

          print("confirm secret-key")
          secret_confirmed = input()
# confirming if the password entered was right
          while secret_created != secret_confirmed:
              print('invalid key entered')
              print('re-enter your secret-key')
              secret_created = getpass()
              print("confirm your secret-key")
              secret_confirmed = getpass()
 # if the code details entered was okay,the following code will run
          else:
                print("Account created successfully")
                print("\n")
                print("you can now log in)
                print("enter username")
                username =input()
                print("enter secret-key")
                secretkey = getpass()
          while username !=username_created or secret_created != secretkey:
                print('invalid details')
                print('enter username')
                username = input()
                print('enter secret-key')
                secretkey = getpass()
   # if the details entered is correct, then the user has to receive the below message


          else:
              print("you are welcomed:{username}") 

   # if the user wants to login to the system ,the following code will run
       elif detail_holder =="log in":
          print("its nice to see you again,welcome")
          print('enter username')
          second_username =input()
          print('enter secret-key')
          second_secret_key = getpass()
            
                
if __name__=="__main__":
  main()
