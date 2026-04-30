print()
def pattern(n):
    if n == 0:
        return
    pattern(n - 1)

    for i in range(n):
        print(" * ", end=" ")
    print()
n=(int(input("Enter a number: ")))
print()