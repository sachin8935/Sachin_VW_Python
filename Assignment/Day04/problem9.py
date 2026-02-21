# 3) Number Guessing Game
# The goal of this game is to guess a secret number chosen by the computer within a limited number of attempts.
# Game Rules:
# • 	The computer randomly selects a number within a predefined range (e.g., 1 to 100).
# • 	The player has a fixed number of attempts (e.g., 7 tries) to guess the correct number.
# • 	After each guess:
# • 	If the guessed number is greater than the actual number, the game will display:
# "Too high! Try a smaller number."
# • 	If the guessed number is less than the actual number, the game will display:
# "Too low! Try a larger number."
# • 	If the player guesses the number correctly within the allowed attempts, they win the game.
# • 	If the player fails to guess the number within the given attempts, the game ends with a loss message revealing the correct number.

import random
num = random.randint(1,100)
guess=7
message="loss"
while (guess!=0):
      input_num = int(input(f"Enter number of your choice you have {guess} attempt left "))
      if(input_num==num):
          print("Congrats you wont the game")
          message="win"
          break
      elif(input_num>num):
           print("Too High! Try a smaller number")
      else:
           print("Too Low Try a higher number")
      guess-=1  

if(message=="loss"):
     print(f"The number was {num} You lost!")
 