print()
name= input("enter your name: ")
greet = lambda x: print("hello", x)
greet (name)
print()
even_odd = lambda x: "even" if x%2 == 0 else "odd"
num = int(input("enter a number: "))
print(even_odd(num))
print()
arith = lambda x, y: (x+y, x-y,x+y, x/y)
num1 = int(input("enter first number: "))
num2 = int(input("enter first number: "))
print(arith(num1, num2))
print()

print()
mylist =[1,2,3,4,5,6]
even = filter(lambda x : x%2 == 0, mylist)
print(list(even))
print()

print()
mylist = [1,2,3,4]
double = map(lambda x: x * 2, mylist)
print()

print()
mynewlist =(list(double))
division = map(lambda x: x//2, mynewlist)
print(list(division))
print()
from functools import reduce
mylist =[1,2,3,4]
mul = reduce (lambda x,y: x*y,mylist)
print(mul)
print()
