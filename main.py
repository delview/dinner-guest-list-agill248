import random # For the Recommended thing
# This is a Dinner Guest List

# Create a invitation Function
def invitation_greet(guest: str):
    print(f"Hello {guest}, you are hearby invited to my Dinner with lots of Tacos and Sour Cream.")

# Create a Remove Guest Function 
def remove_guest(invited_people: list, guest: str):
    if guest in invited_people:
        invited_people.remove(guest)
        print("{guest} has been removed from your spectacualar Dinner!")
    else:
        print("Please select a guest who is in your list and that you want to kick out from the Dinner.")
    return invited_people

# Create a Function that shows the player the Invited List
def display_guest(invited_people: list):
    if invited_people:
        print("\nHere is your current guest list!")
        for guest in invited_people:
            print("{guest}")
    else:
        print("\nYour guest list is empty.")

# Create a Function that tells the user a random recommended thing to do at the Dinner
def recommend_thing():
    things = [
        "Make sure you have enough plates, forks and spoons.",
        "Don't forget the winning speech!",
        "Greet your guests with a smile.",
        "Don't grab all the food at once and leave some for your guests!"
    ]
# Replace Function that will Replace a person the user does not like
def replace_guest(invited_people: list):
    display_guest(invited_people)
    
    guest_remove = input("\nEnter the name of the guest you would like to replace? ").strip()
    if guest_remove not in invited_people:
        print(f"{guess_remove} is not in the guest list!")
        return

    new_guest = input("Enter the name of the new guest:")
# Make a list of People Invited
invited_people = []

# Ask the User the amount of guests to invite
while True:
    try:
        num_guests = input("How many guests would you like to invite?")
        if num_guests <= 0:
            print("Please enter a positive number so that we can continue.")
        else:
            break      
    except ValueError:
        print("Invalid input! Please enter a number!")

# Retrieve guest names
