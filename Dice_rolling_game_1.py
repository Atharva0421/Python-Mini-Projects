                                               #Dice_rolling_game_

# FROM PROGRAMMING WITH MOSH

#use loop (for continue asking)
# Ask: Roll the dice?
# If user enter y
    # generate tow random number
    #print them
# If user enter n
#    print thank you msg
#    terminate
# If user enter anything else 
#     print invalid

import random

while True:
    choice=input("Roll the dice ? (Y/N): ").lower()
    if choice =="y":
        dia1=random.randint(1,6)
        dia2=random.randint(1,6)
        print(f"({dia1},{dia2})")
    elif choice =="n":
        print("Thank you")
        break 
    else:
        print("Invalide choice!")
