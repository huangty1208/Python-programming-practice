#  File: ISBN.py

#  Description: This program will verify the correctness of the ISBN

#  Student Name:  TienYu Huang

#  Student UT EID: th23897

#  Course Name: CS 303E

#  Unique Number: 53465

#  Date Created: 4/15/14

#  Date Last Modified: 4/15/14

############################################################################


def main():
  s1=[]
  s2=[]
  openfile=open("isbn.txt","r")
  outfile=open("isbnOut.txt","w")
  read=openfile.readline()
  while read!="":
    
    readlist=[]
    s1=[]
    for chr in read.rstrip("\n"):
      if chr.isdigit()==False and chr != "x" and chr!="X" and chr!="-":
        break
      else:
        if chr=="X" or chr =="x":
          readlist.append(10)
        elif chr=="-":
          continue
        else:
          readlist.append(int(chr))

    if len(readlist)!=10:
      print(read.rstrip("\n")+"  invalid")
      outfile.write(read.rstrip("\n")+"  invalid"+"\n")
    else:
      for chr in range(1,len(readlist)+1):
        s1.append(sum(readlist[0:chr]))

      if sum(s1)%11==0:
        print(read.rstrip("\n")+"  valid")
        outfile.write(read.rstrip("\n")+"  valid"+"\n")
      else:
        outfile.write(read.rstrip("\n")+"  invalid"+"\n")
        print(read.rstrip("\n")+"  invalid")
      

    read=openfile.readline()
  openfile.close()
  outfile.close()

  outfile=open("isbnOut.txt","r")
  x=outfile.read()
  print(x)
  outfile.close()
main()


