#  File: CreditCard.py

#  Description: This program will test whether a given 16-digit credit card number is valid or not.

#  Student Name:  TienYu Huang

#  Student UT EID: th23897

#  Course Name: CS 303E

#  Unique Number: 53465

#  Date Created: 2/5/14

#  Date Last Modified: 2/5/14

############################################################################

def main():
    #request the card number from the user
    card_number=int(input("Please enter your 16 digits card number "))
    #get individual number from the card by Integer Division
    d1=card_number // 10**15 % 10
    d2=card_number // 10**14 % 10
    d3=card_number // 10**13 % 10
    d4=card_number // 10**12 % 10
    d5=card_number // 10**11 % 10
    d6=card_number // 10**10 % 10
    d7=card_number // 10**9 % 10
    d8=card_number // 10**8 % 10
    d9=card_number // 10**7 % 10
    d10=card_number // 10**6 % 10
    d11=card_number // 10**5 % 10
    d12=card_number // 10**4 % 10
    d13=card_number // 10**3 % 10
    d14=card_number // 10**2 % 10
    d15=card_number // 10**1 % 10
    d16=card_number // 10**0 % 10
    #do the Luhn's Test:
    #Multiply odd digit by 2 and sum digits
    d1=d1*2
    d3=d3*2
    d5=d5*2
    d7=d7*2
    d9=d9*2
    d11=d11*2
    d13=d13*2
    d15=d15*2
    sum_d1 = (d1 % 10) + (d1 // 10)
    sum_d3 = (d3 % 10) + (d3 // 10)
    sum_d5 = (d5 % 10) + (d5 // 10)
    sum_d7 = (d7 % 10) + (d7 // 10)
    sum_d9 = (d9 % 10) + (d9 // 10)
    sum_d11 = (d11 % 10) + (d11 // 10)
    sum_d13 = (d13 % 10) + (d13 // 10)
    sum_d15 = (d15 % 10) + (d15 // 10)

    final_sum=(d2+d4+d6+d8+d10+d12+d14+d16+sum_d1+sum_d3+sum_d5+sum_d7+sum_d9+sum_d11+sum_d13+sum_d15)
    
    print("Enter 16-digit credit card number:",card_number)
    print(" ")
    
    # Final validity test for the sum of digits
    if final_sum % 10 != 0:
        print("Invalid credit card number")     
    else :
        print("Valid credit card number")
        if (card_number//10**15) % 10 == 4:
            print("VISA")
        elif card_number//10**14 == 50 or 51 or 52 or 53 or 54 or 55:
            print("MasterCard")


main()

