
import random
class Management:

    def __init__ (self, age, height, athletic_ability, weight, recommended_position):
        self.age = age
        self.height = height
        self.athletic_ability = athletic_ability
        self.weight = weight
        self.recommended_position = recommended_position


    def __str__(self):
        return (f"Personal_Info:\nAge- {self.age}\nHeight- {self.height}\nAthletic_Ability- {self.athletic_ability}\n"
                f"Weight- {self.weight}")

    def set_position(self, age, height, athletic_ability, weight):
        if self.age and self.height and self.athletic_ability and self.weight:
            words = ("LW", "LM", "ST", "CF", "RW", "RM", "CM", "CDM", "CAM", "LB", "LWB", "CB", "RWB", "RB")
            self.recommended_position = random.choice(words)


    def set_age(self, age):
        self.age = age

    def set_height(self, height):
        self.height = height

    def set_athletic_ability(self, athletic_ability):
        self.athletic_ability = athletic_ability

    def set_weight(self, weight):
        self.weight = weight