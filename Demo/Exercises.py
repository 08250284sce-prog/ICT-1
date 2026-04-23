print()
def calculate_total(m1,m2,m3):
    return m1+m2+m3

def calculate_average(total):
    return total/3
def check_even_odd(num):
    if num % 2==0:
        return "Even"
    else:
        return "Odd"

m1 = float(input("enter the marks of the subject 1:"))
m2 = float(input("enter the marks of the subject 2:"))
m3 = float(input("enter the marks of the subject 3:"))

total = calculate_total(m1,m2,m3)
average = calculate_average(total)

print("total: ", total)
print(f'Average: , {average:.2f}')
if average >= 50:
    print( "pass")
else:
    print( "fail")
num = int(input("Enter the number to check even /odd: "))  
print("The number is: ",check_even_odd(num))  
print()     
