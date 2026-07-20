class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        # TODO: Implement this method
        # It should decrease the pet's hunger by 1
        my_pet.hunger = my_pet.hunger - 1
        
        # and print a message about feeding the pet
        print (f"{my_pet.name} has been fed.")
        print (f"{my_pet.name}'s hunger level: {my_pet.hunger}")

# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times
my_pet.feed()
my_pet.feed()
my_pet.feed()