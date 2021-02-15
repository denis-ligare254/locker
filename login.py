# creating a class,it creates the blueprint for the pearson who will use the susyem
class logins:
   user_info =[]
   def __init__(self,user_credentials,secret_key):
    '''
    instantiation

    '''
    self.user_credentials = user_credentials
    self.secret_key = secret_key
    # the users details have to be saved somewhere,here we have to create a fuction to help us do so
   def save_input(self):
       logins.user_info.append(self)