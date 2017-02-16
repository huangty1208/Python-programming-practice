import math
def sum():
    n=eval(input("input the n", ))
    fact=0
    for i in range(n+1):
        f=i**3
        fact=fact+f
    print("this is the sum",fact)

sum()
