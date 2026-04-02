print()
student_name = input("Enter student name: ")
ndbb = int(input("Enter the of days the book was borrowwd: "))
ndbl = int(input("Enter the number of days late to return: "))
if ndbl <= 0:
    print("you have no due.")
elif ndbl <=5:
    fine = ndbl * 5
    print("You have to pay total due Nu. ",fine,)
elif ndbl<= 10:
    fine = ndbl * 10
    print("you have to pay total due Nu. ",fine,)
else:
    fine = ndbl * 20
    print("You have to pay total due Nu. ",fine,)
if ndbl<= 30:
    print("WARNING:Library privileges may be restricted.")
    print("Please return or get extra duration.")
else:
    pass
print()    
  