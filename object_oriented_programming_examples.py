class Animals:
    count = 0
    def __init__(self, name, age, species= None, family= None):
        self.__name = name
        self._age = age
        self.__species = species
        self.__family = family
    def sound(self):
        print(f"{self.name} is making a sound to indicate it is fron {self.species}")


class Dog(Animals):
    def __init__(self, name, age,colour, shape, species=None, family=None):
        super().__init__(name, age, species, family)
        self.colour = colour
        self.shape = shape
        #Animals.count += 1
my_dog = Dog("Iroh", 4, "brown" ,"four legs", "German shephard", "Carnivorous")

#my_dog.sound()
#print(my_dog)
#print(my_dog.shape)
#print(my_dog.colour)
#print(my_dog.shape)

my_dog.__name = 'John'
