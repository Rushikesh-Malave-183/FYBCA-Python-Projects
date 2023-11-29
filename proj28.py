# Funtions - Greatest of 3 numbers
def check(num1, num2, num3):
    if num1>num2:
        if num1>num3:
            print("A is the greatest.")
        else:
            print("C is the greatest.")
    else:
        if num2>num3:
            print("B is the greatest.")
        else:
            print("C is the greatest.")
a = float(input("Enter any number a: "))
b = float(input("Enter any number b: "))
c = float(input("Enter any number c: "))
check(a,b,c)
