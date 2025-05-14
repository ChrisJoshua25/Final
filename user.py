import main as m

class user:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

self.age = [
    user(f"{m.user_age}")
]


# import main
# import entry_cats from main
# import tkinter as tk
#
#
# window = tk.Tk()
#
# def submit_button(event):
# 	print (f"Welcome {main.entry_cats} to the one place where you will actually improve!")
#
#
# # Bind keypress to event handle_keypress()
# window.bind("<Key>", submit_button)
#
# def button_click(event):
#     print(f"Welcome {main.entry_cats} to the one place where you will actually improve!")
#
#
# button = tk.Button(text="Please don't click me")
# button.bind("<Button-1>", button_click)
# button.pack()