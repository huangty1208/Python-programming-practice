#  File: Benford.py

#  Description: This program will verify Benford's law for the US Census data of 2009.

#  Student Name:  TienYu Huang

#  Student UT EID: th23897

#  Course Name: CS 303E

#  Unique Number: 53465

#  Date Created: 4/27/14

#  Date Last Modified: 4/27/14

############################################################################


def main():
  # create a empty list to include population numbers
  pop_num = []
  # open input file
  inFile = open ("Census_2009.txt", "r")
  # count the overall town or village numer
  count = 0
  # read line by line and skip the header line
  for line in inFile:
    if (count == 0):
      count += 1
      continue

    else:
      count += 1
  # strip the new line charachter from each line 
      line = line.strip()
  # create a list from string of each line
      word_list = line.split()
  # append the last element, the population, to a new list
      pop_num.append (word_list[-1])
  inFile.close()

  # create a dictionary that create a frequency distribution of the the first digit of the population numbers.
  count_dic={}
  for i in range(1,10):
    digit_count=0
    for j in pop_num:
  # reverse the population number to get the first digit 
      rev_pop=j[::-1]
      lead_digit=int(rev_pop)%10
  # increment the count if the header is equal to the assigned digit
      if i==lead_digit:
        digit_count+=1
  # assign the total count to each number from 1 to 9
    count_dic[i]=digit_count

  # print the result
  print("Digit	Count	%")
  for i in count_dic:
    print("%d"%i+"\t"+"%-d"%count_dic[i]+"\t"+"%-0.1f"%(100*(count_dic[i]/(count-1))))

  # Benford's law is verified
main()


