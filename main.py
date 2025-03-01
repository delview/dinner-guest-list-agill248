import random # For the Recommended thing
# This is a Dinner Guest List
 

# Create a Remove Guest Function 
def remove_guest(invited_people: list, guest: str):
    if guest in invited_people:
        invited_people.remove(guest)
        print(f"{guest} has been removed from your spectacualar Dinner!")
    else:
        print("Please select a guest who is in your list and that you want to kick out from the Dinner.")
    return invited_people

# Create a Function that shows the player the Invited List
def display_guest(invited_people: list):
    if invited_people:
        print("\nHere is your current guest list!")
        for guest in invited_people:    
            print(f"{guest}")
    else:
        print("\nYour guest list is empty. Get some people on there!")

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
        print(f"{guest_remove} is not in the guest list!")
        return
    new_guest = input("Enter the name of the new guest:")
    invited_people.remove(guest_remove)
    invited_people.append(new_guest)
    print(f"{guest_remove} spot has been taken over by {new_guest}!")
# Make a list of People Invited
invited_people = []

# Greet the User
print("Hello, welcome to the Dinner Guest Invitation Game!")
name = input("Before we begin what is your name?")
print(f"Welcome {name}, lets start inviting people and make the TACOS!")

# Ask the User the amount of guests to invite
while True:
    try:
        num_guests = int(input("How many guests would you like to invite?"))
        if num_guests <= 0: # FIX THIS AT HOME IT DIDNT WORK
            print("Please enter a positive number so that we can continue.")
        else:
            break      
    except ValueError:
        print("Invalid input! Please enter a number!")

# Retrieve guest names
for x in range(num_guests):
    guest_name = input("Enter the name of the guest you would like to invite to your party!").strip()
    invited_people.append(guest_name)

# Make a choice selection menu for the user
while True:
    print("Okkk, here are the next choices for your party.. By the way I don't know anyone on your list!")
    print("1")