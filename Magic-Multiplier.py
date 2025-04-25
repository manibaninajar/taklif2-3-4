# Get a number from the user
number = int(input("Enter a number: "))

# Print the multiplication table up to 12
for i in range(1, 13):
    result = number * i
    print(f"{number} x {i} = {result}")
