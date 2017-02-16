def pairStar(str):
  if len(str)<=1:
    return(str)
  else:
    if str[0]==str[1]:
      return(str[0]+"*"+pairStar(str[1:]))
    else:
      return(str[0]+allStar(str[1:]))
pairStar("adjacent")
