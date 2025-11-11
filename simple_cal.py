# import math

# def addition (a, b, c):
#     #This function is used to add three numbers
#     return a + b + c

# def subtraction (a, b, c):
#     #This function is used to subtract three numbers
#     return a - b - c

# def multiplication (a, b, c):
#     #This function is used to multiply three numbers
#     return a * b * c

# def division (a, b, c):
#     #This function is used to divide three numbers
#     if b == 0 or c == 0:
#         return "Error: Division by zero is not allowed."
#     if a == 0:
#         return 0
#     return a / b / c

# def area_of_circle(radius):
#     #This function is used to calculate the area of a circle
#     pi = math.pi
#     return pi * radius * radius

# def area_of_rectangle(length, width):
#     #This function is used to calculate the area of a rectangle
#     return length * width

# def area_of_triangle(base, height):
#     #This function is used to calculate the area of a triangle
#     return 0.5 * base * height

# def average_of_a_number(a, b, c):
#     #This function is used to calculate the average a number
#     return (a + b + c)/3

# print("The addition of the number is" + addition (2,3,4))

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = first_number + second_number
    print("The result of addition is: {}".format(result))
elif operation == '-':
    result = first_number - second_number
    print("The result of subtraction is: {}".format(result))
elif operation == '*':
    result = first_number * second_number
    print("The result of multiplication is: {}".format(result))
elif operation == '/':
    if second_number != 0:
        result = first_number / second_number
        print("The result of division is: {}".format(result))
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation! Try again.")