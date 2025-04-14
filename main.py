import user
# import tkinter as tk
#
# window = tk.Tk()
print("Welcome to the best app for atheltic improvement! Please fill out the needed information to continue.")

def athletic_options():
    user_choice = input("""
    "Info" - Information of Self
    "General" - General Improvements
    "Position" - Positional Improvements
    "Skills" - Skills
    "Stop" - Log Out
    """)

    return user_choice


user_choice = athletic_options()

if user_choice.lower() == "stop":
    print("You have successfully logged out of your session! Sadly, your account is terminated becuase you \n"
          "should never have logged out in the first place! Ok, bye bye.")
    exit()

while user_choice.lower() != "stop":
    if user_choice.lower() == "info":
        user_input = input()

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
