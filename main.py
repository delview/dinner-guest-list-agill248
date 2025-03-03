import random # For the Recommended thing
# This is a Dinner Guest List
 

# Create a Add Guest Function
def add_guest(invited_people: list):
   while True:
        guest = input("Please enter the name of the guest you would like to invite!").strip()
        if guest:
            invited_people.append(guest)
            print(f"{guest} has been added!")
            break
        else:
         print("Please enter in the right name for the sake of your guest!")

# Create a Remove Guest Function 
def remove_guest(invited_people: list):
    while True:
        guest = input("Please enter the name of the guest you would like remove!").strip()
        if guest in invited_people:
            invited_people.remove(guest)
            print(f"{guest} has been removed from your spectacualar Dinner!")
            break
        elif guest == "":
            print("That is an invalid, please enter in the correct name!")
        else:
            print("That guest isn't on your list silly, please try again!")

# Create a Function that shows the player the Invited List
def display_guest(invited_people: list):
    if invited_people:
        print("\nHere is your current guest list!")
        for guest in invited_people:    
            print(f"{guest}")
    else:
        print("\nYour guest list is empty. Get some people on there!")

# Create a Send Invite Function 
def send_invites(invited_people: list):
    print("\nSending Invitations.")
    for guest in invited_people:
        print(f"The Invitation has been sent to {guest}")
    print("ALL OF YOUR INVITATIONS HAS BEEN SEND!")
    if not invited_people:
        print("There are no guests to invite!")
        return
# Create a Function that tells the user a random recommended thing to do at the Dinner
def recommend_thing():
    things = [
        "Make sure you have enough plates, forks and spoons.",
        "Don't forget the winning speech!",
        "Greet your guests with a smile.",
        "Don't grab all the food at once and leave some for your guests!"
    ]
    print(random.choice(things))
# Replace Function that will Replace a person the user does not like
def replace_guest(invited_people: list):
    display_guest(invited_people)
    guest_remove = input("\nEnter the name of the guest you would like to replace? ").strip()
    if guest_remove not in invited_people:
        print(f"{guest_remove} is not in the guest list! (just because of that your restarting....)")
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
    print("\nHere are the next choices for your party.. (1) Add guest, (2) Remove guest, (3) View your list, (4) Recommended things to do at the party, (5) Replace a guest, (6) Send out invites and (7) Exit.")
    choice = input("Please select a option.").strip()

    if choice == "1":
        invited_people = add_guest(invited_people)
    elif choice == "2":
        remove_guest(invited_people)
    elif choice == "3":
        display_guest(invited_people)
    elif choice == "4":
        recommend_thing()
    elif choice == "5":
        replace_guest(invited_people)
    elif choice == "6":
        send_invites(invited_people)
    elif choice == "7":
        print("Peace out and have a wonderful party! LIVE IT UP!")
        break
    else:
        print("Please select one of the seven choices, by using a number.")

        