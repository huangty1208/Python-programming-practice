def main():
    total = 0
    n=eval(input("how many numbers are there?"))
    for i in range(1,4*n,4):
        total = (4/i)-4/(i+2)+ total
    print("The approximate is", total)
 
main()
