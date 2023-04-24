from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Rock Paper Scissors")
root.resizable(width = False , height = False)

# Set the images
rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((200, 200)))
paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((200, 200)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((200, 200)))

# Create the buttons
rock_button = Button(root, image=rock_img, command=lambda: set_choice("rock"))
paper_button = Button(root, image=paper_img, command=lambda: set_choice("paper"))
scissors_button = Button(root, image=scissors_img, command=lambda: set_choice("scissors"))

# Create the labels
user_label = Label(root, text="You", font=("Helvetica", 20))
computer_label = Label(root, text="Computer", font=("Helvetica", 20))
user_image_label = Label(root)
computer_image_label = Label(root)

# Place the widgets on the screen
user_label.grid(row=0, column=0)
computer_label.grid(row=0, column=2)
user_image_label.grid(row=1, column=0)
computer_image_label.grid(row=1, column=2)
rock_button.grid(row=2, column=0, padx=10, pady=10)
paper_button.grid(row=2, column=1, padx=10, pady=10)
scissors_button.grid(row=2, column=2, padx=10, pady=10)

# Define the set_choice function
def set_choice(choice):
    # Set the user's choice image
    if choice == "rock":
        user_image = rock_img
    elif choice == "paper":
        user_image = paper_img
    else:
        user_image = scissors_img
    user_image_label.config(image=user_image)

    # Set the computer's choice image
    computer_choice = random.choice(["rock", "paper", "scissors"])
    if computer_choice == "rock":
        computer_image = rock_img
    elif computer_choice == "paper":
        computer_image = paper_img
    else:
        computer_image = scissors_img
    computer_image_label.config(image=computer_image)

    # Determine the winner and display the result
    if choice == computer_choice:
        result = "It's a tie!"
    elif (choice == "rock" and computer_choice == "scissors") or \
         (choice == "paper" and computer_choice == "rock") or \
         (choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "Computer wins!"
    messagebox.showinfo("Result", result)

    # Clear the images
    user_image_label.config(image="")
    computer_image_label.config(image="")

root.mainloop()
