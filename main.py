import management as m

from management import Management

import random
words = ["LW", "LM", "ST", "CF", "RW", "RM", "CM", "CDM", "CAM", "LB", "LWB", "CB", "RWB", "RB"]
user_choice = random.choice(words)

management_archive = []
management = m.Management("", "", "", "", "", "")
#import user
# import tkinter as tk
#
# window = tk.Tk()
print("Welcome to the best app for athletic improvement! Please fill out the needed information to continue.")
#This is the HOMEPAGE
def athletic_options():
    user_choice = input("""
    "Info" - Information of Self
    "General" - General Improvements
    "Position" - Positional Improvements
    "Skills" - Skills
    "Stop" - Log Out
    """)

    return user_choice


user_input = athletic_options()
#THIS ENDS THE CODE (IT WORKS)
if user_input.lower() == "stop":
    print("You have successfully logged out of your session! Sadly, your account is terminated because you \n"
          "should never have logged out in the first place! Ok, bye bye.")
    exit()
#THIS STARTS THE INFO SECTION
while user_input.lower() != "stop":
    if user_input.lower() == "info":
        user_info = input("We would like to know some information about you before we continue (It is used to determine "
                          "\nyour position + helps us learn more about our users). Please write 'Yes' if you"
                           "\nwould like to continue and 'No' to go back to the home page. Write 'Exit' if you would like to logout.\n")
        s_flag = False
        while s_flag is False:
            if user_info.lower() == "exit":
                exit()
            s_flag = True
            if user_info.lower() == "no":
                s_flag = True
            if user_info.lower() == "yes":
#THIS IS THE FIRST QUESTION
                user_name = input("What is your name? ")
                print("Ok, welcome " + user_name)
                management_archive.append(management)
                management.set_name(user_name)
                user_age = int(input("How old are you? "))
                if user_age >= 7:
                    print("Ok, this is one of the best times to start playing this sport!")
                    management_archive.append(management)
                elif user_age < 6:
                    print("You are very young to be using this app! Assuming your parents are controlling this account, you\n"
                        "will still be able to use the app features.")
                    management_archive.append(management)
                else:
                    print("You are starting this sports journey pretty late. However, here we do not give up in our clients!\n"
                        "We will make you become one of the best at this sport!")
                management.set_age(user_age)
#THIS ASKS YOUR HEIGHT
                user_height = int(input("How tall are you (in inches)?\n"))
                if user_height >= 60 or user_height <= 61:
                    print("Ok, thank you")
                    s_flag = True
                management.set_height(user_height)
#THIS ASKS FOR YOUR OPINION ON YOUR ATHLETIC ABILITY
                user_athletic = int(input("From a scale of 1-10, what would you rate your athletic ability?\n"))
                if user_athletic <= 5:
                    print("You shouldn't rate yourself so low!... but thank you for your honesty.")
                elif user_athletic > 5:
                    print("Ok, you seem to be decent in your sport, let's see if we can make you better!")
                    s_flag = True
                management.set_athletic_ability(user_athletic)
#THIS ASKS YOUR WEIGHT
                user_weight = int(input("How much do you weigh? (In lbs)\n"))
                if user_weight <= 1:
                    print("Ok, thank you!")
                    s_flag = True
                management.set_weight(user_weight)
                print(management)
#THIS SHOULD PROVIDE A RANDOM POSITION
                user_position = input("We used the information you have given us to determine the best position for you!\n"
                                      "Would you like it to be shown? (yes or no):\n")
                if user_position == "yes":
                    print("Great!")
                    user_choice = random.choice(words)
                    s_flag = True
                elif user_position == "no":
                    print("The question was honestly a courtesy, I'm adding it regardless. :)")
                    user_choice = random.choice(words)
                    s_flag = True
                management.set_position(user_choice)
                print(management)


#HERE, THE USER WILL HAVE ACCESS TO VIDEOS ABOUT GENERAL THINGS A SOCCER PLAYER MUST KNOW HOW TO DO
    elif user_input.lower() == "general":
        user_general = input("You have now opened the General Tab! Here we provide you with videos to improve in your "
                               "sport in all areas.\n These include Dribbling, Defending, Shooting, Passing, and Speed.\n"
                               "Would you like to proceed? (yes or no)\n")
        s_flag = False
        while s_flag is False:
            if user_general.lower() == "yes":
                print("Dribbling: (https://youtu.be/jwIHc9rz7yo?si=TkoaKbqZPPzpOTRO)\n"
                        "Defending: (https://youtu.be/5DkFpmCrCWY?si=GfPJEyKjQ8OnFXZU)\n"
                        "Shooting: (https://youtu.be/tcoRi1OxFmo?si=TTwPcaxQhEedExr_)\n"
                        "Passing: (https://youtu.be/xvaD2AamMpU?si=YIjtKo6irkpWgtA5)\n"
                        "Speed: (https://youtu.be/1enUeG0i3Gw?si=23NEhNXY1_kj2AAi)\n"
                      "All of these will show you different techniques where you will be able to improve in your skill.")
                s_flag = True
            elif user_general.lower() == "no":
                s_flag = True


#HERE THE PERSON WILL CHOOSE WHAT THEY BELIEVE IS THE BEST POSITION FOR THEMSELVES
    elif user_input.lower() == "position":
        positions = ["CB", "LB", "LWB", "RWB", "RB", "CM", "CAM", "CDM", "LW", "LM"
                    , "RW", "RM", "CF","ST"]
        user_choice = input("Please tell us the position you would like to play! (PLEASE USE THE ABBREVIATION FOR THE POSITION)\n"
                            "(CB, LB, LWB, RWB, RB, CM, CAM, CDM, LW, LM, RW, RM, CF, ST):\n")
        s_flag = False
        while s_flag is False:
            if user_choice.upper() in positions:
                print(f"Ok, you believe that your designated position is {user_choice}\n")
                #user_choice  user_position
                s_flag = True
                management.set_position(user_choice)
                print(management)

#IN ADDITION TO GENERAL, THE USER WILL HAVE ACCESS TO VIDEOS ON HOW TO DO SKILLS THAT CAN BE USED IN A SOCCER GAME
    elif user_input.lower() == "skills":
        user_skill = input("You have entered the SKILLS section of the application! Here we provide you with videos where\n "
                           "you can learn different skills. Would you like to proceed? (yes or no):\n")
        s_flag = False
        while s_flag is False:
            if user_skill.lower() == "yes":
                print("Trivela: (https://youtu.be/bR3HZbvSMwY?si=x7sfWPsSIqlsFueP)\n"
                      "Scissors: (https://youtu.be/YtbwfWxcfT4?si=-ubvcwq7cyaR2w7Z)\n"
                      "Body Feint: (https://youtu.be/OX4WUr3TCfA?si=HHevNCCQ1JbyHygp)\n"
                      "Step-Over: (https://youtu.be/b7P5MBS6yhc?si=exr_9Gf6KE5UrqVf)\n")
                s_flag = True
            elif user_skill.lower() == "no":
                s_flag = True

    else:
        print("Not an option!")
    user_input = athletic_options()