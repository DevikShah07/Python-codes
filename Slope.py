x1=int(input("Write your x1:"))
x2=int(input("Write your x2:"))
y1=int(input("Write your y1:"))
y2=int(input("Write your y2:"))

z=x2-x1



if z==0:
    print("the slope is vertical line")
else:
    slope=(y2-y1)/(x2-x1)
    print(slope)
    if slope>0:
        print("slope is negative")
    elif slope<0:
        print("slope is positive")
    elif slope==0:
        print("the slope is horizontal line")
