print()
for i in range(1,4):
    for j in range(i):
        print(f"outer loop iteration{i},inner loop iteration{j+1}")
print()
for i in range(4):
    for j in range(i):
        print("*", end = " ")
    print()
print()    
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end = " ")
    print()    
print()
for i in range(6,0,-1):
    for j in range(1,i):
        print("1", end = " ")
    print()    
print()    
    
