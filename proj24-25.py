# Natural numbers
n = int(input("Enter the value of n: "))
for i in range(1, n + 1):
    print(i, end=", ")

# Even numbers
start = int(input("\nEnter the starting number: "))
end = int(input("Enter the ending number: "))
if start%2 != 0:
    start += 1
if end%2 != 0:
    end += 1
for i in range(start, end + 1, 2):
    print(i, end=", ")
