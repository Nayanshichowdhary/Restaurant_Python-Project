# define the menu of restaurant
menu ={
   'Pizza':40,
   'Pasta':50,
    'Cream Roll':10,
    'Burger':30,
    'chai or coffee':80,
    'Salad':60  
 }

print("Welcome to Chowdhary Restaurant")
print("Pizza: RS 40\nPasta: RS 50\nCream Roll: RS 10\nBurger: RS 30\nchai or coffee: RS 80\nSalad: RS 60")

order_total = 0
# 10+30=40

item_1 = input("Entre the name of item you want to order = ")
if item_1 in menu:
      order_total += menu[item_1] # 0+40 
      print(f"your item {item_1} has been added to your order")
      
else:
   print(f"ordered item{item_1} is not avaiable yet!..")

another_order = input("Do you want to add another item?? (Yes/No)")
if another_order == "Yes":
   item_2 = input("Entre the name of second item = ")
if item_2 in menu:
   order_total += menu[item_2]
   print(f"item {item_2} has been added to your order")
else:
   print(f"this order item{item_2} is not available yet..")
   
print(f"the total amount of items to pay is{order_total}")

   

      