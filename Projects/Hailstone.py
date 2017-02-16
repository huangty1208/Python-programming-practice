#  File: Hailstone.py

#  Description: This program will verify the conjecture in a user defined range. Once the beginning and ending of the range have been verified, the program will compute the cycle length for each of the numbers in that range inclusive of the end points. The program will print out the number that has the largest cycle length and what that cycle length is. 

#  Student Name:  TienYu Huang

#  Student UT EID: th23897

#  Course Name: CS 303E

#  Unique Number: 53465

#  Date Created: 3/2/14

#  Date Last Modified: 3/2/14

############################################################################

def main():
  # prompt the user to enter the first number of the range and the last number.
  start_n=eval(input("Enter starting number of the range: "))

  # check if both numbers are positive (> 0) individually and that the first number in the user defined range is less than or equal to the last number in that range. 
  while start_n <0 :
    print("Please enter a positive number")
    start_n=eval(input("Enter starting number of the range: "))

  end_n=eval(input("\n"+"Enter ending number of the range: "))
  while end_n < 0 or end_n < start_n:
    print("Please enter a number bigger or eual to starting number")
    end_n=eval(input("Enter ending number of the range: "))
  
  # define biggest count, and the number with the largest cycle length

  biggest_count = 0
  largest_num = 0

  # program will compute the Hailstone cycle length (count) for each of the numbers in that range inclusive of the end points.
  for i in range(start_n,end_n+1):
    current_num=i
    count = 0
    while i != 1 :
  # Take any natural number n. If n is even, divide it by 2 to get n / 2. If n is odd, multiply by 3 and add 1 to obtain 3 n + 1.
      if i % 2 ==0 :
        i=i/2
        count+=1
      else :
        i=i*3+1
        count+=1
  # compare the cycle count of each number and retain the larger number
    if count > biggest_count :
      biggest_count= count
      largest_num = current_num
      
  # print out the number that has the largest cycle length and what that cycle length is.
  print("\n"+"The number", largest_num, "has the longest cycle length of", biggest_count,end=".\n")


main()

