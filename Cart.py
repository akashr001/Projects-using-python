class Cart:

    def __init__(self, items ,choices):
        self.Choices = choices
        self.FoodItems = self.__AddtoCart(items)


    def __AddtoCart(self, items):
        foodDic = {}
        for choice in self.Choices:

            if choice > len(items):
                return KeyError

            if choice in foodDic:
                foodDic[choice]+=1

            else:
                foodDic[choice]=1
        return foodDic

    def Processorder(self, Fooditems):

        Total = 0

        for item in self.FoodItems:#item is key
            price = self.FoodItems[item]*Fooditems[item-1].Price
            Total +=price
            print(f"{Fooditems[item-1].Name} x {self.FoodItems[item]} = {price}")

        print(f"Total : {Total}")
        self.Processpayment(Total)


    def Processpayment(self,Total):
        print(f"Your Total for the payment {Total}")
        print("1:Cash on delivery, 2:Debit card")
        opt = int(input("Enter a choice:"))
        if opt == 1:
            print("You select a cash on delivery option the delivery partner reach you soon")
        elif opt == 2:
            print("Your choosing debit card you will transfer to payment gateway shorty")

        print("<<< Thanks for using our online food ordering system!!! >>>")








