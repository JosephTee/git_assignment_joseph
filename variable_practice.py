lst = list(range(20,25))
print(f"The range trial gives you {lst}")

# Task 1: Variables and Operations
name = "Joseph"
age = int(26)
height = float(6.4)

print(f"My name is {name.title()}, I am {age} years old and {height} meters tall")

# Code to check if I am an adult or minor

new_age = age + int(5)# you don't need to use int() to declare an integer per say
new_height = height * 2

if new_age > 18:
    print("Adult")
else:
    print("Minor")


# Task 2: For Loops

#Code toprint number from 1 to 20
print("\nRange calculation")
for i in range(20):
    print(i + int(1))

# Code to print only even numbers.
print("\nstarting even number")
for i in range(21):
    if i % 2 == 0:
        print(i)

# Create a list of five scores (integers). Use a for loop to print each score and check if it is greater than 50
print("\nStarting my number code")
my_num_list = [59, 30, 45, 12, 600]
for score in my_num_list:
    if score > 50:
        print(f"The number is {score}")
        print("Pass")
    else:
        print(f"The number is {score}")
        print("Fail")


#\n Task 3: While Loops
print("\n While loop cal")
initial_num= 0
user = int(input("Enter a number: "))
while user != 0:
    initial_num += user
    user = int(input("Enter a number: "))
    
print(f"The total sum you got is {initial_num}")
if initial_num > 100:
    print("Great Job")
else:
    print("Keep Trying")



#\n Task 4: Combined Loops and Conditionals
print("\nStarting Task 4: Combined Loops and Conditionals")
for i in range(1,51):
    if i % 3== 0 and i%5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)

# Task 5: Mini Project - Simple Calculator
print("\nStarting Task 5: Mini Project - Simple Calculator")
first_number = float(input("Enter your first number: "))
second_number = float(input("Enter your second number: "))
Operation = input("Which operation are you doing! enter: +, -, *, /")
if Operation == "+":
    print(first_number + second_number)


