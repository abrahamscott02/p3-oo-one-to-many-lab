class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if pet_type not in Pet.PET_TYPES:
            raise Exception("pet_type is not in PET_TYPES")

        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Th pet must be an instance of Pet.")

        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)






#     @classmethod
#     def otherMethod(cls):
#         x = cls("Joe")
#         print("Hello owners")

# o = Owner("Bob")

# # o = Owner()
# # o.__init__("Bob")

# o.myMethod()
# Owner.otherMethod()