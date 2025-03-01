class House:

    houses_history = []

    def __new__(cls, *args):
        print(args)
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        isinstance(new_floor, int)
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")

    def __eq__(self, other):
        isinstance(other, int)
        return self.number_of_floors == other

    def __lt__(self, other):
        isinstance(other, int)
        return self.number_of_floors < other

    def __le__(self, other):
        isinstance(other, int)
        return self.number_of_floors <= other

    def __gt__(self, other):
        isinstance(other, int)
        return self.number_of_floors > other

    def __ge__(self, other):
        isinstance(other, int)
        return self.number_of_floors >= other

    def __ne__(self, other):
        isinstance(other, int)
        return self.number_of_floors != other

    def __add__(self, value):
        isinstance(value, int)
        new_House = House(self.name, self.number_of_floors + value)
        return new_House

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __del__(self):
        print (f"{self.name} снесён, но он останется в истории")

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)


del h2
del h3

print(House.houses_history)