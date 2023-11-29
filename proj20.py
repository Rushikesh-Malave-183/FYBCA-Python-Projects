# Sum of series
userInput = input("Enter your series seperated with a comma: ")
numbers = [int(num) for num in userInput.split(',')]
totalSum = 0
for i in numbers:
    totalSum = totalSum + i
print("The sum of the given series is:", totalSum)
