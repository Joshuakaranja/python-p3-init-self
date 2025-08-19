#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed


# manual test block
if __name__ == "__main__":
    fido = Dog("Fido", "Dalmatian")
    spot = Dog("Spot")  # should default to "Mutt"
    
    print(fido.name, fido.breed)  # Fido Dalmatian
    print(spot.name, spot.breed)  # Spot Mutt

    pass