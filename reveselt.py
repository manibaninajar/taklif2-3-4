# 1. Get input from the user
text = input("Please enter a string: ")

# 2. Create an empty string to store the reversed text
reversed_text = ""

# 3. Start from the last character and go backwards
i = len(text) - 1  # Index of the last character

while i >= 0:
    reversed_text = reversed_text + text[i]  # Add the character to the result
    i = i - 1  # Move one step back

# 4. Print the reversed string
print("Reversed string:", reversed_text)
