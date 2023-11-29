# Fibonacci series
numA = 1
numB = 2
nos = int(input("Enter the amount of Fibonacci elements you need: "))/2
print("The required fibonacci series is: ")
for i in range(0,int(nos+1)):
    print(str(numA)+", "+str(numB), end=(", "))
    numA = numA + numB
    numB = numA + numB

