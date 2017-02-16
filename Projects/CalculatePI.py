#  File: CalculatePI.py

#  Description: This program will calculate PI using random numbers to simuluate the throwing of darts.

#  Student Name:  TienYu Huang

#  Student UT EID: th23897

#  Course Name: CS 303E

#  Unique Number: 53465

#  Date Created: 3/23/14

#  Date Last Modified: 3/23/14

############################################################################

import math
import random

def computePI ( numThrows ):
  # define the number of times a dart lands within the circle
  dart_incircle = 0
  
  #　use the unput parameter as the number of throws on the dartboard
  for i in range(numThrows):

  # specify a random point inside the dart board by its x and y coordinates
    xPos = random.uniform (-1.0, 1.0)
    yPos = random.uniform (-1.0, 1.0)

  # determine if a point is inside the circle. Increment count if it is. 
    if math.hypot (xPos, yPos) < 1 :
      dart_incircle += 1

  # That count divided by the total number of throws is the ratio π/4
  cal_pi = (dart_incircle/numThrows) * 4 
  
  return(cal_pi)

def main():
  # see if the accuracy of PI increases with the number of throws on the dartboard.
  num_list = [100, 1000, 10000, 100000, 1000000, 10000000]

  for numThrows in num_list : 

    cal_pi= computePI(numThrows)
    difference = math.pi - cal_pi 
    print("num =",numThrows, "\t"+"Calculated PI =",round(cal_pi,6), "\t"+"Difference =",round(difference,6))
 
main()


