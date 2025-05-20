
class Management:

    def __init__ (self, name, age, height, athletic_ability, weight, recommended_position):
        self.name = name
        self.age = age
        self.height = height
        self.athletic_ability = athletic_ability
        self.weight = weight
        self.recommended_position = recommended_position


    def __str__(self):
        return (f"Personal_Info:\nAge- {self.age} years old\nHeight- {self.height} inches tall\nAthletic_Ability- {self.athletic_ability}/10\n"
                f"Weight- {self.weight}lbs\nPosition We Recommend- {self.recommended_position}")

    def set_position(self, recommended_position):
    #     if self.age and self.height and self.athletic_ability and self.weight:
    #         words = ("LW", "LM", "ST", "CF", "RW", "RM", "CM", "CDM", "CAM", "LB", "LWB", "CB", "RWB", "RB")
        self.recommended_position = recommended_position

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_height(self, height):
        self.height = height

    def set_athletic_ability(self, athletic_ability):
        self.athletic_ability = athletic_ability

    def set_weight(self, weight):
        self.weight = weight