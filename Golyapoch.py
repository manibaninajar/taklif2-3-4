import random

print("Welcome to the Flower or Empty game!")
print("Pick left or right.")

flower = random.choice(["left", "right"])

choice = input("Enter 'left' or 'right': ").lower()

if choice == "left" or choice == "right":
    if choice == flower:
        print("Congratulations! You found the flower.")
    else:
        print("Empty! The flower was in the", flower)
else:
    print("Invalid input! You must enter 'left' or 'right'.")
