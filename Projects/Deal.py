#  File: Deal.py

#  Description: This program will simulate the game show and demonstrate that indeed Marilyn vos Savant gave sensible advice to switch the door.

#  Student Name:  TienYu Huang

#  Student UT EID: th23897

#  Course Name: CS 303E

#  Unique Number: 53465

#  Date Created: 3/17/14

#  Date Last Modified: 3/17/14

############################################################################

import random

def main():
  #  prompt the user to enter the number of times he or she wants to play this game
  times=eval(input("Enter number of times you want to play: "))

  # create a variable to keep track of the number of times the contestant wins by switching
  win_switching = 0

  # print categories
  print("\n"+" Prize      Guess       View    New Guess ")

  # run this simulation for however many times the user had specified.

  for i in range(times):

  # Generate a random number between 1 and 3 (inclusive) that will denote the door that conceals the prize
    prize = random.randint(1,3)

  # Generate another random number between 1 and 3 (inclusive) that will denote the guess the contestant makes.
    guess = random.randint(1,3)

  # compute a number that does not conceal the prize nor is it the contestant's guess. This is the door that is opened by Monty Hall and we shall call it view.
    view =  random.randint(1,3)
    while view == prize or view == guess :
      view = random.randint(1,3)
    
  # At this point the contestant changes his mind makes a newGuess that is not the original guess nor is it the view
    newGuess = random.randint(1,3)
    while newGuess == guess or newGuess == view :
      newGuess = random.randint(1,3)

  # print out Prize, Guess, View, New Guess
    print("  ",prize,"        ",guess,"        ",view,"        ",newGuess)

  # compare the value of the newGuess with that of prize. If they are the same, the contestant won by switching, and you increment the variable that was keeping track of that.
    if newGuess == prize :
      win_switching += 1

  # To obtain the probability for winning if switched divide the number of times the contestant wins by switching by the total number of games played.
  winprob_switch = win_switching / times

  # To obtain the probability of winning by not switching subtract the above number from one.
  winprob_noswitch = 1 - winprob_switch

  # print out both probabilities
  print("\n"+"Probability of winning if you switch =",round(winprob_switch,2))
  print("Probability of winning if you do not switch =",round(winprob_noswitch,2))

  
 
main()

