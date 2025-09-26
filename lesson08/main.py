class Animal:
    name = ""
    __age = 0

    def make_sound(self):
        raise NotImplemented("Error!")
    
    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value >= 0:
            self.__age = value
        else:
            print("Error!")

    def info(self):
        print(f"Ім'я: {self.name}, Вік: {self.__age}")

class Lion(Animal):

    def make_sound(self):
        print(f"Ррррр!")


class Elephant(Animal):

    def make_sound(self):
        print(f"Тууу!")


class Parrot(Animal):

    def make_sound(self):
        print(f"Чирик-чирик!")



class Zoo:
    animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, name):
        self.animals.remove(name)

    def show_animals(self):
        for a in self.animals:
            a.info()

    def make_all_sounds(self):
        for a in self.animals:
            a.make_sound()


lion1 = Lion()
lion1.name = "Лев"
lion1.set_age(5)

elephant1 = Elephant()
elephant1.name = "Слон"
elephant1.set_age(11)

parrot1 = Parrot()
parrot1.name = "Папуга"
parrot1.set_age(2)

animals = [lion1,elephant1,parrot1]

zoo = Zoo()
zoo.animals = animals
zoo.remove_animal(elephant1)
zoo.add_animal(lion1)
zoo.add_animal(elephant1)
zoo.show_animals()
zoo.make_all_sounds()