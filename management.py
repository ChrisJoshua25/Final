class Management:


    def __init__ (self, age, height, athletic_ability, weight):
        self.age = age
        self.height = height
        self.athletic_ability = athletic_ability
        self.weight = weight


    def __str__(self):
        return (f"Personal_Info: Age- \n{self.age}\n, Height- {self.height}\n, Athletic_Ability- {self.athletic_ability}\n"
                f", Weight- {self.weight}")

    def set_age(self, age):
        self.age = age

    def set_height(self, height):
        self.height = height

    def set_athletic_ability(self, athletic_ability):
        self.athletic_ability = athletic_ability

    def set_weight(self, weight):
        self.weight = weight