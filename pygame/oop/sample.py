class Dog:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        if self.gender == "boy":
            print(f"{self.name}, Good Boy, eatUp")
        else:
            print(f"{self.name}, Good Girl, eatUp")

    def bark(self, loud):
        if loud == True:
            print("WOOF WOOF WOOF WOOF")
        else:
            print("WOOF")


class Beagle(Dog):
    def __init__(self, name, age, gender, gunShy):
        super().__init__(name, age, gender)

    def hunt(self):
        print("hunting")


beagle_1 = Beagle("beagle_1", 11, "boy")
beagle_1.bark(True)
beagle_1.hunt()


# dog_1 = Dog("jessi", 5, "girl")
# dog_2 = Dog("peter", 3, "boy" )
# dog_1.eat()
# dog_2.eat()
# dog_1.bark(True)
# dog_2.bark(False)
