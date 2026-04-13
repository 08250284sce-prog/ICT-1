print()
li = ["python programming","python fundamental","python questions"]
for x in li:
    print(x)
print()  
lenli = len(li) 
for x in range(lenli): 
    print(li[x])
print()

tuple_list = tuple(li)
for x in tuple_list:
    print(x)
print()    
Set_list = set(li)
for x in Set_list:
    print(x)
print()
tup = ("John Smith", "Jane Doe", "Ailce Johnson")
for x in tup:
    print(x)
set1 = {10, 30, 20}   
for x in set1:
    print(x)
print()    
BookDetails = dict({"python programming": "john simth","python fundamentals": "Alice johnson", "python interview questions":"jane doe"})
for keys in BookDetails:
    print(keys,BookDetails[keys])
print()    



