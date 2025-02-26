# This is a Dinner Guest List

# Create a invitation Function
def invitation_greet():
    print(f"Hello {invited_people}, you are hearby invited to my Dinner with lots of Tacos and Sour Cream.")

# Create a Remove Guest Function 
def remove_guest(invited_people: list, guest: str):
    if guest in invited_people:
        invited_people.remove(guest)
        print("That guest has been removed from your spectacualar Dinner!")
    else:
        print("Please select a guest who is in your list and that you want to kick out from the Dinner.")
    return invited_people

# Create a Function that shows the player the Invited List
def display_guest(invited_people: list):
    if invited_people:
        print("\nHere is your current guest list!")

# Make a list of People Invited
invited_people = []

