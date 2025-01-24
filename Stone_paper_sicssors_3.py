# Ask user to make a Choice 
# if choice is not valid 
# print KeyError
# let the computer to make a Choice
# print choice
# determine the winner
# ask user if they want to continue
# id not
#   then terminate 

import random

emojis={"r":"🪨", "p":"🧻","s":"✂️"}   # use dict
choices=("r","p","s")

while True:

    user_choice=input("Choose between Rock,Paper,Sicssors (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invaild choice!")
        continue  # use for if invaild choice it not terminat  the program it will work continue

    computer_choice= random.choice(choices)
    print(f"You Choose{emojis[user_choice]}")
    print(f"Computer Choose{emojis[computer_choice]}")

    if user_choice==computer_choice:
        print("Tiee!")
    elif(
        (user_choice=="r" and computer_choice=="s") or
        (user_choice=="s" and computer_choice=="p")or
        (user_choice=="p"and computer_choice=="r")):
            print("You Win!!")
    else:
        print("You Lose!!")

    should_continue=input("Do you want continue (y/n): ").lower().strip()#Added .strip() after .lower() to ensure no extra spaces accidentally break the comparison 
                                                                          #(e.g., input() might capture a trailing space like "n ").
    if should_continue =="n":
         print("Thank You")
         break

    