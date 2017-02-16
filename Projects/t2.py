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

    print(a,b,c,d)

    #compute the following quantities to get the day of the week
    w = (13 * a - 1 ) // 5
    x = c // 4
    y = d // 4
    z = w + x + y + b + c - 2 * d
    r = z % 7
    r = (r + 7) % 7


    
main()
