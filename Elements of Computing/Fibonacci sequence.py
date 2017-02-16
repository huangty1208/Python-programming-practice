def main():
    a,b = 1,1
    n=eval(input("Please input what Fib number you want to be calculated: "))
    for i in range(n-2):
        a,b=b,a+b
    print(b)

main()
