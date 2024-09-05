class Pet:
    all = []
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise ValueError(f"Invalid pet type: {pet_type}. Must be one of {self.PET_TYPES}.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

    def __repr__(self):
        return f"Pet(name={self.name}, pet_type={self.pet_type}, owner={self.owner.name if self.owner else 'None'})"
    pass



class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of pets that belong to this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Add a pet to the owner and Pet.all list."""
        if not isinstance(pet, Pet):
            raise ValueError("Only Pet instances can be added.")
        
        if pet not in Pet.all:
            Pet.all.append(pet)
        
        pet.owner = self

    def get_sorted_pets(self):
        """Return a list of pets owned by this owner, sorted by pet name."""
        return sorted(self.pets(), key=lambda pet: pet.name)

    def __repr__(self):
        return f"Owner(name={self.name})"
    pass