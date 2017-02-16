def main():
    total = 0
    num = eval(input("What are the numbers you have? "))
    for i in num:
        total = i + total 
    print("The total value of your numbers are", total)
 
main()
