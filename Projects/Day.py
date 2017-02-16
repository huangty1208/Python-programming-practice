#  File: Day.py

#  Description: This program will prompt the user to enter the day, month, and year. The program will print out the day of the week for that date. 

#  Student Name:  TienYu Huang

#  Student UT EID: th23897

#  Course Name: CS 303E

#  Unique Number: 53465

#  Date Created: 2/17/14

#  Date Last Modified: 2/17/14

############################################################################

def main():
    #request the year(c), month(a), and day(b) from the user
    c=int(input("Enter year: "))
    a=int(input("Enter month: "))
    b=int(input("Enter date: "))
    

    #make the make the adjustment so the year begins in March and ends in February
    if a < 3:
        a=a+10
        c=c-1
    else :
        a=a-2

    #get the century based on the year
    d=c//100
    c=c%100

    #compute the following quantities to get the day of the week
    w = (13 * a - 1 ) // 5
    x = c // 4
    y = d // 4
    z = w + x + y + b + c - 2 * d
    r = z % 7
    #to take care of negative values of r
    r = (r + 7) % 7 

    #Write a chained conditional to find the day of the week based on r
    if (r == 0):
        print("\n"+"The day is Sunday.")
    elif (r == 1):
        print("\n"+"The day is Monday.")
    elif (r == 2):
        print("\n"+"The day is Tuesday.")
    elif (r == 3):
        print("\n"+"The day is Wednesday.")
    elif (r == 4):
        print("\n"+"The day is Thursday.")
    elif (r == 5):
        print("\n"+"The day is Friday.")
    elif (r == 6):
        print("\n"+"The day is Saturday.")
    else:
        print("\n"+'Invalid day')


main()

