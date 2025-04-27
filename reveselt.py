# Get text from the user
text = input("Enter a text: ")

# Create an empty string to store the reversed text
reversed_text = ""

# Use a for loop to go from the end of the text to the beginning
for i in range(len(text) - 1, -1, -1):
    reversed_text = reversed_text + text[i]

# Print the reversed text
print(reversed_text)
