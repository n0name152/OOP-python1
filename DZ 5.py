class Animal:
    def __init__(self, breed):
        self.breed = breed
class WalkerAnimal:
    def __init__(self, walk_speed):
        self.walk_speed = walk_speed
    def walk(self):
        return f"Walking at {self.walk_speed} km/h"
class SwimmerAnimal:
    def __init__(self, swim_speed):
        self.swim_speed = swim_speed

    def swim(self):
        return f"Swimming at {self.swim_speed} km/h"


class MultiAnimal(Animal, WalkerAnimal, SwimmerAnimal):
    def __init__(self, breed, walk_speed, swim_speed):
        Animal.__init__(self, breed)
        WalkerAnimal.__init__(self, walk_speed)
        SwimmerAnimal.__init__(self, swim_speed)

Crocodile = MultiAnimal("Crocodile", 3, 10)


def show_abilities(self):
    return f"I am a {self.breed}. {self.walk()} and {self.swim()}"

print(show_abilities(Crocodile))