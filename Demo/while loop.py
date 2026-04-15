no_of_students = int(input("Enter the number of student"))
student_names = {}
while i <= no_of_students:
    name  = input("Enter the name of student:")
    print("The name of student {} is {}".format(i,name))
    i +=1
    student_names[i] = name
print("The list of students is: " , student_names)
print()
while True:
    print("This is an infinite loop. press ctrl+c to stop it.")
print("===="*24)
# loop control statement
print()
for i in range(4):
    if i == 2:
        break
    print(i)
for i in range (4):
    if i ==2:
        continue
    print(i)   
print("loop ened") 
print("====="*24)   



