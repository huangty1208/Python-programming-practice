def main():
    total = 0
    n=eval(input("how many numbers are there?"))
    num = eval(input("What are the numbers you have? "))
    for i in num:
        total = i + total
        avg=total/n
    print("The average of your numbers is", avg)
 
main()
