import random

print("Welcome to the Flower or Empty game!")
print("Pick a number between 1 and 2.")

flower = random.randint(1, 2)

choice = int(input("Enter your number: "))

if choice == flower:
    print("Congratulations! You found the flower.")
else:
    print("Empty! The flower was at number", flower)
