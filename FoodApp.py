from Models.User import User
from Models.usermanager import usermanager
from Controllers.MainMenu import MainMenu

class LoginSystem:
        def Login(self):
            mailid = input("Email Id : ")
            password = input("password : ")

            user=usermanager.FindUser(mailid, password)
            if user is not None:
                print("login successfully")
                menu = MainMenu()
                menu.start()
            else:
                print("Invalid mailid/password...please retry")

        def Register(self):
            #In memory collection is used to store the user details
            name = input("Name : ")
            mobile = int(input("Mobile No : "))
            mailid=input("Email Id : ")
            password=input("password : ")

            user =User(name,mobile,mailid,password)
            usermanager.AddUser(user)

        def GuestLogin(self):
            pass

        def exit(self):
            print("Thank you for using our food app")
            exit()

        def ValidateOption(self,option):
                #built in method #without bracket it checks the variables not a method
                getattr(self,option)()
                #print("enter invalid choice")







class FoodApp:

    LoginOptions = {1:"Login",2:"Register",3:"Guest",4:"Exit"}

    @staticmethod
    def Init(): #Initial method
        print("<< WELCOME TO ONLINE FOOD ORDERING >>")




        loginSystem1=LoginSystem()

        while True:
           for option in FoodApp.LoginOptions:
              print(f"{option}.{FoodApp.LoginOptions[option]}",end=" ")

           print()
           try:
               choice=int(input("please Enter your choice :"))
               loginSystem1.ValidateOption(FoodApp.LoginOptions[choice])

           except (ValueError,KeyError):#string is given as input value error and dictionary key not present means key error
                print("invalid input...please enter valid choice")


