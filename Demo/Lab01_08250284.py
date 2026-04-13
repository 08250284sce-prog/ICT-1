print()
student_list = [] 
student_age = set()
student_grade = set()
student_dict = {}

student_list.append("Sonam")
student_list.append("Kelzang")
student_list.append("Pema")
student_list.append("Dechen")
student_age.add(24)
student_age.add(28)
student_age.add(25)
student_age.add(27)
student_grade.add('A')
student_grade.add('D')
student_grade.add('C')
student_grade.add('B')
student_dict['Sonam'] = {'age': 24, 'grade': 'A'}
student_dict['Kelzang'] = {'age': 28, 'grade': 'D'}
student_dict['Pema'] = {'age': 25, 'grade': 'C'}
student_dict['Dechen']= {'age': 27, 'grade': 'B'}

add_student = input("Enter the student name to add or else enter to skip: ") 
add_age = int(input("Enter the age of the student: ")) 
add_grade = input("Enter the grade of the student: ") 
if add_student: 
    student_list.append(add_student) 
    student_age.add(add_age)
    student_grade.add(add_grade) 
    student_dict[add_student] = {'age': add_age, 'grade': add_grade} 
    print(f"Student added successfully! The age of the student '{add_student}' is {student_dict[add_student]['age']} and the grade is {student_dict[add_student]['grade']}.")
else:
    print("No student added")
print()
search_name = input("Enter the student name to search: ")
if search_name in student_list:
    print(f"Student found! The age of the student '{search_name}' is {student_dict[search_name]['age']} and the grade is {student_dict[search_name]['grade']}.") 
    print("Student not found")
    print()
    remove_student = input("Enter the student name to remove or else enter to skip: ")
    remove_age = student_dict[remove_student] 
    remove_grade = student_dict[remove_student] 
    student_list.remove(remove_student) 
    del student_dict[remove_student] 

    print("Student removed successfully!") 
    print("Students left along with their details: ", student_dict) 
    print("List of students left: ", student_list) 
else: 
    print("Student not found") 
print()