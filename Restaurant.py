from Models.abstractitem import AbstractItem
from Models.FoodMenu import FoodMenu


class Restaurant(AbstractItem):

    def __init__(self, name, location, offer, rating):
        super().__init__(name, rating)
        self.Location = location
        self.Offer = offer
        self.__FoodMenus = []

    @property
    def FoodMenus(self):

          return self.__FoodMenus

    @FoodMenus.setter
    def FoodMenus(self, items):

      for item in items:
         if not isinstance(item, FoodMenu):
             print("Invalid Foodmenu..")
             return
      self.__FoodMenus = items

    def DisplayItem(self, start):
        print(f"{start} => {self.Name} >>Rating :{self.Rating}")

