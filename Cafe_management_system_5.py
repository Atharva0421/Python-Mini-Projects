# create dictionay for menu

menu={
    "pizza":40,
    "pasta":50,
    "burger":70,
    "salad":60,
    "coffee":80,
}

#Greet 
print("🎊 WELCOME TO PYTHON RESTURANT 🎊")
print("Menu for you =")
print("PIZZA🍕: 40.RS \nPASTA🍝: 50.RS\nBURGER🍔: 70.RS\nSALAD🥗: 60.RS\nCOFFEE☕: 80.RS")

total_order=0
#item1+item2 it display the tolat order 

item_1=input("Enter the name of item you want to order: ")
if item_1 in menu:
    total_order +=menu[item_1] #0+50  0+item rs
    print(f"Your item {item_1} has been added to order")
else:
    print(f"Ordered item {item_1} not available yet")

another_order=input("Do you want to add another item (yes/No): ")
if another_order=="Yes".lower():
    item_2=input("Enter the name of second item: ")
    if item_2 in menu:
        total_order+=menu[item_2]
        print(f"Item {item_2} has been added to order ")
    else:
        print(f"Order item {item_2} not availabel yet")

print(f"Total amount of item is {total_order}.RS💵")

