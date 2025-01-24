# Number_guessing_game_

#generate a random number
# ask user to enter a number gusse
#if not a vaild number 
# print an Error
# if number < guess
# print too low
# if number < guess
# else print well done


# import random

# number_to_guess=random.randint(1,100)
# while True:

#     try:
#         guess=int(input("Enter The Guess Between the 1 to 100: "))
#         if guess < number_to_guess:
#             print("Too Low!!")
#         elif guess > number_to_guess:
#             print("Too High!!")
#         else:
#             print(f"Congrtulation ,You guess correct number {guess}")
#             break
#     except ValueError:             # use for to if any case use enter str (alphabet)
#         print("Please Enter Valid Number")

import random
numbers_to_guess=random.randint(1,100)
enter_guesss=-1   # use for true condition always true
guess=1

while(enter_guesss!=numbers_to_guess): 
    enter_guesss==int(input("Enter the Guess between 1 to 100: "))

    if(enter_guesss > numbers_to_guess):
        print("Lower number please")
        guess+=1
    elif(enter_guesss < numbers_to_guess):
        print("Higher number please")
        guess+=1 # guess=guess+1
print(f"You guess the number correctl is {numbers_to_guess} in {guess} attempts")

  