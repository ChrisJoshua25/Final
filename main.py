import management as m

from management import Management

management_archive = []
management = m.Management("", "", "", "")
import user
# import tkinter as tk
#
# window = tk.Tk()
print("Welcome to the best app for athletic improvement! Please fill out the needed information to continue.")

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

if user_input.lower() == "stop":
    print("You have successfully logged out of your session! Sadly, your account is terminated because you \n"
          "should never have logged out in the first place! Ok, bye bye.")
    exit()

while user_input.lower() != "stop":
    if user_input.lower() == "info":
        user_info = input("We need to know some information about you before we continue. Please write 'Yes' if you"
                           "\nwould like to continue. Otherwise, write 'No' and log out!\n")
        s_flag = False
        while s_flag is False:
            if user_info.lower() == "yes":
                user_age = int(input("How old are you? "))
                if user_age >= 7:
                    print("Ok, this is one of the best times to start playing this sport!")
                elif user_age < 6:
                    print("You are very young to be using this app! Assuming your parents are controlling this account, you\n"
                        "will still be able to use the app features.")
                else:
                    print("You are starting this sports journey pretty late. However, here we do not give up in our clients!\n"
                        "We will make you become one of the best at this sport!")
            elif user_input.lower() == "no":
                exit()
            s_flag = True

            user_height = int(input("How tall are you (in inches)?\n"))
            if user_height >= 60 or user_height <= 61:
                print("Ok, thank you")
                s_flag = True

            user_athletic = int(input("From a scale of 1-10, what would you rate your athletic ability?\n"))
            if user_athletic <= 5:
                print("You shouldn't rate yourself so low!... but thank you for your honesty.")
            elif user_athletic > 5:
                print("Ok, you seem to be decent in your sport, let's see if we can make you better!")
            s_flag = True
            print(management)
            user_input = athletic_options()

    elif user_input.lower() == "general":
        user_general = input("You have now opened the General Tab! Here we provide you with videos to improve in your "
                               "sport in all areas.\n These include Dribbling, Defending, Shooting, Passing, and Speed.\n"
                               "Would you like to proceed?")
        s_flag = False
        while s_flag is False:
            if user_general.lower() == "yes":
                print("Dribbling: (INSERT THE LINK)\n"
                        "Defending: (INSERT THE LINK)\n"
                        "Shooting: (INSERT THE LINK)\n"
                        "Passing: (INSERT THE LINK)\n"
                        "Speed: (INSERT THE LINK)\n")
                s_flag = True
            elif user_general.lower() == "no":
                s_flag = True
                user_input = athletic_options()

# First Tab (Survey)

# entry_cats = ['First Name: ', 'Last Name: ']
#
# entry_frame = tk.Frame(
#     relief=tk.SUNKEN, borderwidth=3
# )
# entry_frame.pack(padx=5, pady=5)
#
# button_frame = tk.Frame(
# )
# button_frame.pack(fill=tk.X, ipadx=5, ipady=5)
#
# for i, text in enumerate(entry_cats):
#     label = tk.Label(master=entry_frame, text=text)
#     entry = tk.Entry(master=entry_frame, width=75)
#
#     label.grid(row=i, column=0, sticky="e")
#     entry.grid(row=i, column=1)
#
# submit_button = tk.Button(
#     master=button_frame,
#     text="Submit",
#     width=10,
#     height=2
# )
# submit_button.pack(side=tk.RIGHT, padx=10, pady=10)
# clear_button = tk.Button(
#     master=button_frame,
#     text="Clear",
#     width=10,
#     height=2
# )
# clear_button.pack(side=tk.RIGHT, padx=10, pady=10)
#
#
#
# window.mainloop()
