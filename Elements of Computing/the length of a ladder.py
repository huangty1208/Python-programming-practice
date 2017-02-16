import math
def length():
    height, angle=eval(input("input the height and angle seperated by comma"))
    radians=math.pi*angle/180
    length=height/math.sin(radians)
    print("this is the length",length)

length()
