def main():
    x=eval(input("what is the number that you want for square root?"))
    n=eval(input("how many guesses you want?"))
    guess=x/2
    for i in range(n):
        guess=(guess+x/guess)/2
        print("The approximate square root is", guess)
 
main()
