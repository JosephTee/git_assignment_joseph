class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"The name of my restaurant is {self.restaurant_name}")
        print(f"The meal we have is {self.cuisine_type}")
    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open today!")

restaurant_from_my_class = Restaurant('Country Kitchen', 'Fast food')
print(f"My restaurant name is: {restaurant_from_my_class.restaurant_name}")
print(f"We sell {restaurant_from_my_class.cuisine_type} meal here!")
print()
restaurant_from_my_class.describe_restaurant()
restaurant_from_my_class.open_restaurant()
print()
print()
restaurant_from_my_school = Restaurant('Captain Cook', 'Bread and Beans')
print(f"My restaurant name is: {restaurant_from_my_school.restaurant_name}")
print(f"We sell {restaurant_from_my_school.cuisine_type} meal here!")
print()
restaurant_from_my_school.describe_restaurant()
restaurant_from_my_school.open_restaurant()

