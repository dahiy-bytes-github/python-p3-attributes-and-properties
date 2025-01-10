class Dog:
    APPROVED_BREEDS = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]

    def __init__(self, name="unknown", breed="Mastiff"):
        self.name = name  # Will call set_name due to property
        self.breed = breed  # This will call the setter for 'breed'

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and (0 < len(name) <= 25):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    # Defining name as a property
    name = property(get_name, set_name)
    
    # Getter for breed
    def get_breed(self):
        return self._breed

    # Setter for breed
    def set_breed(self, breed):
        if breed in self.APPROVED_BREEDS:  # Accessing class variable
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    # Defining breed as a property
    breed = property(get_breed, set_breed)
