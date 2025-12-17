class Restaurant:
    call_count = 0
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"The name of my restaurant is {self.restaurant_name}")
        print(f"The meal we have is {self.cuisine_type}")
        Restaurant.call_count += 1
    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open today!")
        Restaurant.call_count += 1

    @classmethod
    def total_calls(cls):
        print(f"Total method calls so far: {cls.call_count}")

if __name__ == '__main__':
    restaurant_from_my_class = Restaurant('Country Kitchen', 'Fast food')
    print()
    restaurant_from_my_class.describe_restaurant()
    restaurant_from_my_class.open_restaurant()
    print()
    restaurant_from_my_school = Restaurant('Captain Cook', 'Bread and Beans')
    print()
    restaurant_from_my_school.describe_restaurant()
    restaurant_from_my_school.open_restaurant()
    Restaurant.total_calls()