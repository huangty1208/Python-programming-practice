#  File: Cipher.py

#  Description: This program will use a simple algorithm to encrypt and decrypt the transposition cipher.

#  Student Name:  TienYu Huang

#  Student UT EID: th23897

#  Course Name: CS 303E

#  Unique Number: 53465

#  Date Created: 4/4/14

#  Date Last Modified: 4/4/14

############################################################################


def main():
  # prompt the user to enter whether he wants to encrypt or decrypt. 
  decision=input("Do you want to encrypt or decrypt? (E / D): ")

  # read the contents of the file input.txt as a single string and then encrypt it
  if decision.lower()== "e":
    openfile=open("input.txt","r")
    content=openfile.read()
    
  # form two strings - one with all the characters in the even locations starting at 0 and the other with all the characters in the odd locations.
    even_str=content[::2]
    odd_str=content[1::2]

  # write the encrypted result to the file output.txt
    outputfile=open("output.txt","w")
    outputfile.write(odd_str+even_str)

  # close the file 
    openfile.close()
    outputfile.close()

  # print result message
    print("\n"+"Output written to output.txt")

  # read the contents of the file input.txt as a single string and then decrypt it using the transposition cipher    
  elif decision.lower()== "d":
    openfile=open("input.txt","r")
    content2=openfile.read()

  # decrypt the concatenation of the odd string and the even string
    str_len=len(content2)
    
    odd_str_op=content2[:int(str_len/2)]
    even_str_op=content2[int(str_len/2):]

  # recombine odd and even strings
    decrypted_str=""

    for i in range(int(str_len/2)+1):
      decrypted_str += even_str_op[i:i+1]+odd_str_op[i:i+1]

  # write the encrypted result to the file output.txt
    outputfile=open("output.txt","w")
    outputfile.write(decrypted_str)

  # close the file 
    openfile.close()
    outputfile.close()

  # print result message
    print("\n"+"Output written to output.txt")

  # If the user does not enter the correct response, write an error message as specified and exit the program by doing a return.
    
  else:
    print("\n"+"Wrong input. Bye.")
    return()

main()


