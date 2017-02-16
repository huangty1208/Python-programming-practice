def main():
  x=[]

  l=[0,1,3,1,6,2,9,5,9,10]
  for i in range(1,len(l)+1):
    x.append(sum(l[0:i]))
  print(x)


main()
