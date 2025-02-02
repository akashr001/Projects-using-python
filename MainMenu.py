from Controllers.FoodManager import FoodManager
from Models.Cart import Cart


class MainMenu:

        __Options = {1: "Show Restaurants", 2: "Show FoodItems", 3: "Search Restaurant",4:"Search FoodItem", 5 : "Logout"}


        def __init__(self):
            self.__FoodManager = FoodManager()

        def ShowRestaurants(self):
            for i,res in enumerate(self.__FoodManager.Restaurants,1):
                res.DisplayItem(i)

            choice = int(input("Please Select the Restaurant :"))
            res = self.__FoodManager.Restaurants[choice-1]
            self.ShowFoodMenus(res.FoodMenus)

        def ShowFoodItems(self, foodItems = None):   # Practice
            if foodItems is not None:
                for i, fooditem in enumerate(foodItems,1):
                    fooditem.DisplayItem(i)
                choices = list(map(int, input("Please enter your food items (eg 1,2) : ").split(',')))
                cart = Cart(foodItems,choices)
                cart.Processorder(foodItems)
            else:
                 pass


        def SearchRestaurant(self):
          pass


        def SearchFoodItem(self):# Practice
            pass

        def ShowFoodMenus(self, menus):
                for i,menu in enumerate(menus,1):#List of collection the number is shown
                    menu.DisplayItem(i)
                choice =int(input("Please choose Menu : "))
                fooditems = menus[choice-1].FoodItems
                self.ShowFoodItems(fooditems)


        def start(self):
            while True:
                 for option in MainMenu.__Options:
                    print(f"{option}.{MainMenu.__Options[option]}", end=" ")
                    print()
                 try:
                     choice = int(input("Please Enter Your Choice: "))
                     value = MainMenu.__Options[choice].replace(" ","")
                     getattr(self,value)()
                 except (ValueError, KeyError):
                     print("Invalid input.. Please Enter the Valid Choice")



