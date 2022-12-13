from Animal import *

class TestAnimal:
    """for each animal, must call eat() and make_noise()"""        
    def __init__(self, name):
        test = Cat(name)
        test.eat()
        test.make_noise()

if __name__ == "__main__":
    for i in ["Whitey", "Blackey", "Pinky", "Bobby"]:
        TestAnimal(i)