#Write a program to calculate the volume and surface area of a sphere from its radius, given as input. 

import math
def volume():
    radius=eval(input("input the radius here"))
    vol=4/3*math.pi*radius**3
	print("this is the answer", vol)	
	

import math
def surface():
    radius=eval(input("input the radius here"))
    sur=4*math.pi*radius**2
    print("this is the answer", sur)
	
	
#Write a program that calculates the cost per square inch of a circular pizza, given its diameter and price. The formula for area is A = .r2
	
import math
def cost():
    diameter,price=eval(input("give the diameter and price here, seperated by comma",))
    area=math.pi*(diameter/2)**2
    cost=price/area
    print("this is the cost per square inch of a circular pizza",cost)
	
#Write a program that determines the molecular weight of a hydrocarbon based on the number of hydrogen, carbon, and oxygen atoms. 
	
#molecular weight
def mol():
    h,c,n=eval(input("input the number of h,c,n here separated by comma",))
    mol= h*1.0079+c*12.011+n*15.9994
    print("this is the molecular weight",mol)

#Write a program that determines the distance to a lightning strike based on the time elapsed between the flash and the sound of thunder. The speed of sound is approximately 1100 ft/sec and 1 mile is 5280 ft.
def distance():
    time=eval(input("input the time elapsed between the flash and the sound of thunder"))
    dis=time*1100/5280
    print("the distance in miles from the flash is",dis)

#The Konditorei coffee shop sells coffee at $10.50 a pound plus the cost of shipping. Each order
#ships for $0.86 per pound + $1.50 fixed cost for overhead. Write a program that calculates
#the cost of an order.
def order():
    pound=eval(input("pounds of coffee you bought",))
    tot=pound*(10.50+0.86)+1.50
    print("the total is",tot)

#Two points in a plane are specified using the coordinates (x1,y1) and (x2,y2). Write a program
#that calculates the slope of a line through two (non-vertical) points entered by the user.
def slope():
    x1,y1,x2,y2=eval(input("input the coordinates(x1,y1) and (x2,y2) seperated by comma",))
    slope=(y2-y1)/(x2-x1)
    print("the slope is",slope)

#Write a program that accepts two points (see previous problem) and determines the distance
#between them.
import math
def distance():
    x1,y1,x2,y2=eval(input("input the coordinates(x1,y1) and (x2,y2) seperated by comma",))
    dis=math.sqrt((x2-x1)**2+(y2-y1)**2)
    print("the distance is",dis)

#Write a program that prompts the user for a 4-digit year and then outputs the value of the
#epact.

def main():
    year = eval(input("Please enter the 4-digit year "))
    c = year//100
    epact = (8+(c//4) - c + (8*c + 13)//25 + 11*(year%19))%30
    print("The Gregorian epact is", epact)
main()
    
#Write a program to calculate the area of a triangle given the length of its three sides a, b, and
#c using these formulas:

import math
def main():
    a,b,c = eval(input("Please enter the length of its three sides a, b, and c"))
    s =(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("the area of a triangle ",area)
main()
    
#Write a program to determine the length of a ladder required to reach a given height when
#leaned against a house. The height and angle of the ladder are given as inputs. 

import math
def length():
    height, angle=eval(input("input the height and angle seperated by comma"))
    radians=math.pi*angle/180
    length=height/math.sin(radians)
    print("this is the length",length)

length()

#Write a program to find the sum of the first n natural numbers, where the value of n is
#provided by the user.


def sum():
    n=eval(input("input the n", ))
    fact=0
    for i in range(n+1):
        fact=fact+i
    print("this is the sum",fact)

sum()

#Write a program to find the sum of the cubes of the first n natural numbers where the value
#of n is provided by the user

def sum():
    n=eval(input("input the n", ))
    fact=0
    for i in range(n+1):
        f=i**3
        fact=fact+f
    print("this is the sum",fact)

sum()

#Write a program to sum a series of numbers entered by the user. The program should first
#prompt the user for how many numbers are to be summed. It should then input each of the
#numbers and print a total sum.
def main():
    total = 0
    num = eval(input("What are the numbers you have? "))
    for i in num:
        total = i + total 
    print("The total value of your numbers are", total)
 
main()

#Write a program that finds the average of a series of numbers entered by the user. As in the
#previous problem, the program will first ask the user how many numbers there are. Note: the
#average should always be a float, even if the user inputs are all ints.
def main():
    total = 0
    n=eval(input("how many numbers are there?"))
    num = eval(input("What are the numbers you have? "))
    for i in num:
        total = i + total
        avg=total/n
    print("The average of your numbers is", avg)
 
main()

#Write a program that approximates the value of . by summing the terms of this series: 
def main():
    total = 0
    n=eval(input("how many numbers are there?"))
    for i in range(1,4*n,4):
        total = (4/i)-4/(i+2)+ total
    print("The approximate is", total)
 
main()

#A Fibonacci sequence is a sequence of numbers where each successive number is the sum of
#the previous two. The classic Fibonacci sequence begins: 1, 1, 2, 3, 5, 8, 13,. . .. Write a
#program that computes the nth Fibonacci number where n is a value input by the user. 
def main():
    a,b = 1,1
    n=eval(input("Please input what Fib number you want to be calculated: "))
    for i in range(n-2):
        a,b=b,a+b
    print(b)

main()

#to write your own algorithm for computing square roots.
#One way to solve this problem is to use a guess-and-check approach. You first guess what
#the square root might be and then see how close your guess is. 
def main():
    x=eval(input("what is the number that you want for square root?"))
    n=eval(input("how many guesses you want?"))
    guess=x/2
    for i in range(n):
        guess=(guess+x/guess)/2
        print("The approximate square root is", guess)
 
main()



