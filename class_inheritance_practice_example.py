"""QUESTION 1: Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write 
a class called IceCreamStand that inherits from the Restaurant class you wrote. 
Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. 
Create an instance of IceCreamStand, and call this method."""

from restaurant_class import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors = None):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors if flavors is not None else []
    def show_flavors(self):
        return f"We serve: {', '.join(self.flavors)}"
    
my_meal = IceCreamStand('John', 'garri', ['vanilla', 'banana', 'mango'])
print(my_meal.show_flavors())

