menu={
    "pizza":40,
    "pasta":80,
    "burger":70,
    "salad":50,
    "coffee":20
}

print("WELCOME TO AKASH'S RESTAURANT")
print("pizza: Rs40\npasta: Rs80\nburger: Rs80\nsalad: Rs50\ncoffee: Rs20")

order_total=0

item_1=input("Enter the name of item you want to order=")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
     print(f"ordered item {item_1} is not available!")

another_order=input("Do you want to add another item? (yes/no)")
if another_order=="yes":
    item_2=input("Enter name of your second item=")
    if item_2 in menu:
      order_total +=menu[item_2]
      print(f"Item {item_2} has been added to your order")
    else:
      print(f"ordered item{item_2}is not available!")

print(f"The total amount of items is to pay {order_total}")
print("--Thanks for visiting our resataurant--\nVisiting Again!!!")
