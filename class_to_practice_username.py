"""Question 1
Restaurant: Make a class called Restaurant. The __init__() method for 
Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of 
information, and a method called open_restaurant() that prints a message indi
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri
butes individually, and then call both methods.

Question 2
Three Restaurants: Start with your class from Exercise 9-1. Create three 
different instances from the class, and call describe_restaurant() for each 
instance.

Question 3
Users: Make a class called User. Create two attributes called first_name 
and last_name, and then create several other attributes that are typically stored 
in a user profile. Make a method called describe_user() that prints a summary 
of the user’s information. Make another method called greet_user() that prints 
a personalized greeting to the user.
Create several instances representing different users, and call both meth
ods for each user."""
class User:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
    def describe_user(self):
        print(f"User details are: \nFirst name = {self.first_name} \nLast name = {self.last_name} \nAge: {self.age} \nSex = {self.sex}")
    
    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello {full_name.title()}! How have you been.")

my_fiance = User('gloria', 'owolabi', 23, 'Female')


my_fiance.describe_user()
my_fiance.greet_user()