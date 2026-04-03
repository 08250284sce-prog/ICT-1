print()
my_tuple = ("Hello",123456)
print(type(my_tuple))
print(my_tuple)
print(my_tuple[1])
a,b=my_tuple
print(b)
new_tuple = tuple(a)
print(new_tuple)
concatenated_tuple = my_tuple + new_tuple
print(concatenated_tuple) #
print(concatenated_tuple[2:6:2])
print(concatenated_tuple[::-1]) #
print(concatenated_tuple[:2]+concatenated_tuple[2:][::-1])
print()

