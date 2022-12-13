class Animal:
    """Animal class: a parent class"""
    def __init__(self, name):
        self.name = name
        print("An animal has been born.")

    def eat(self):
        print("Munch Munch")

    def make_noise(self):
        print(f"Grrr says animal {self.name}.")


class Cat(Animal):
    """Cat class inherits from animal."""
    def __init__(self, name):
        super().__init__(name)
        print("An cat has been born.")
        
    def make_noise(self): # method overriden
        print(f"Meow says {self.name}.")


class Dog(Animal):
    """Dog class inherits from animal."""
    def __init__(self, name):
        super().__init__(name)
        print("A dog has been born.")
        
    def make_noise(self):
        print(f"Bark says {self.name}")

if __name__ == "__main__":
    print("main")
    Cat("delta").make_noise()
    Dog("delta").make_noise()