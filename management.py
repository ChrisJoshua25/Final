class Management:


    def __init__ (self, age, height, athletic_ability, weight):
        self.age = age
        self.height = height
        self.athletic_ability = athletic_ability
        self.weight = weight

    def __str__(self):
        return f"Personal Info: Age- {self.age}\n, Height- {self.height}\n, Athletic_Ability- {self.athletic_ability}\n, Weight- {self.weight}"
