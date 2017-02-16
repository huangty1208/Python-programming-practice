def main():
    #request the year(c), month(a), and day(b) from the user
    i=int(input("Enter number: "))

    count = 0
    while i != 1 :
  # Take any natural number n. If n is even, divide it by 2 to get n / 2. If n is odd, multiply by 3 and add 1 to obtain 3 n + 1.
      if i % 2 ==0 :
        i=i/2
        count+=1
      else :
        i=i*3+1
        count+=1


    print(count)



    
main()
