from os import system
from rich import print

system("clear||cls")

print("[red on white]ESCAPE THE ABANDONED SCHOOL[/red on white]")

print("You wake up inside an abandoned school.")
print("You don't remember how you got there.")
print("All of the doors are locked.")
print("You hear heavy footsteps coming from upstairs.")

print("")
print("What do you want to do next?")
print("1. Explore the hallway")
print("2. Enter the classroom")

choice = input("Make a choice!:")

if choice == "1":
    print("You walk down the dark hallway.")
    print("You see two doors.")
    print("1. Enter the science lab")
    print("2. Hide in the janitor's closet")

    choice2 = input("Make a choice!: ")

    if choice2 == "1":
        print("You enter the science lab.")
        print("You hear something moving behind you.")

    elif choice2 == "2":
        print("You hide in the janitor's closet.")
        print("You find a key sitting on a shelf!")

elif choice == "2":
    print("You enter the creepy classroom.")
    print("You hear a loud bang behind you.")
