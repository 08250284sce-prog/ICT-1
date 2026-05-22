try:
    file = open("students.txt","r")
    students = file.readlines()
    print("student ids:")
    for student in students:
        data=students.strip().split(",")
        print(data[2])
except FileNotFoundError:
    print("Error: The file does not exist.")
except Exception as e:
    print("Unexceted error:",e)
finally:
    try:
        file.close()
        print("File closed successful.")
    except:
        pass
    print("program completed.")
        