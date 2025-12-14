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