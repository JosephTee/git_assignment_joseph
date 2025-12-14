class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

joseph_car = Car('toyota', 'camry', 2026)
print(joseph_car.brand)
joseph_car.brand= "Audi"
print(joseph_car.brand)
print(joseph_car)