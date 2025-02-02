from Models.FoodItem import FoodItem
from Models.FoodMenu import FoodMenu
from Models.Restaurant import Restaurant

class FoodManager:
    def __init__(self):
        self. Restaurants = self.__PrepareRestaurants()

    def __PrepareFoodItems(self):


        item1 = FoodItem("Veg Biriyani",  4,  150, "***")
        item2 = FoodItem("ChickenBiriyani",  4.2,  200,  "***")
        item3 = FoodItem( "Parota",  4.4,  60,  "***")
        item4 = FoodItem("Dosa",  4.1,  50,"***")
        item5 = FoodItem("Noodles", 3.8,  100,  "***")
        return [item1, item2, item3, item4, item5]

    def __PrepareFoodMenus(self):
        FoodItems = self.__PrepareFoodItems()

        menu1 = FoodMenu("Veg")
        menu1.FoodItems = [FoodItems[0], FoodItems[3]]
        menu2 = FoodMenu("Non-Veg")
        menu2.FoodItems = [FoodItems[1], FoodItems[2]]
        menu3 = FoodMenu("Chinese")
        menu3.FoodItems = [FoodItems[4]]
        return [menu1, menu2, menu3]

    def __PrepareRestaurants(self):
        FoodMenus = self.__PrepareFoodMenus()

        res1 = Restaurant("A2b","chennnai",30,7)
        res1.FoodMenus = [FoodMenus[0]]
        res2 = Restaurant( "MuniyandiVilas",  "coimbatore", 70,8)
        res2.FoodMenus = [FoodMenus[0], FoodMenus[1]]

        res3 = Restaurant("Diamond","bangalore",80, 5)
        res3.FoodMenus = [FoodMenus[1], FoodMenus[2]]
        return [res1,res2,res3]

    def FindRestaurant(self, name):
        for res in self.Restaurants:
            if res.Name == name:
                return  res
