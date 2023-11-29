def areaCircle():
    r = float(input("\nEnter the radius of your Circle: "))
    print("The area of your circle is:", 3.1415 * r * r)

def areaSquare():
    s = float(input("\nEnter the length of your square: "))
    print("The area of your square is: ", s * s)

def areaRectangle():
    l = float(input("\nEnter the length of your rectangle: "))
    b = float(input("\nEnter the breadth of your rectangle: "))
    print("The area of your rectangle is: ", l * b)

def areaTriangle():
    b = float(input("Enter the base of your triangle: "))
    h = float(input("Enter the height of your triangle: "))
    print("The area of your triangle is: ", 0.5 * b * h)

print("\nChoose an option:")
print("1. Calculate the area of a Circle")
print("2. Calculate the area of a Square")
print("3. Calculate the area of a Rectangle")
print("4. Calculate the area of a Triangle")
print("5. Exit")

while True:

    choice = input("\nEnter your choice (1/2/3/4/5): ")

    if choice == '1':
        areaCircle()
    elif choice == '2':
        areaSquare()
    elif choice == '3':
        areaRectangle()
    elif choice == '4':
        areaTriangle()
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
