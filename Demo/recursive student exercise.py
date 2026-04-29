print()
def fun(x,y):
    if x == 0:
        return y
    else:
        return fun(x-1,y+x)
x= int(input("enter the x value:"))
y=int(input("enter the y value:"))
print(f"the value of x={x} and y={y} is: {fun(x,y)}")
print()