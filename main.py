# Define a function that takes a string and an integer shift value as parameters  
def shift_string(message: str, shift: int) -> str:
    # Create an empty list to store the shifted characters  
    shifted_chars = []
    # Loop through each character in the string:
    for char in message:
        # If the character is a letter (A-Z or a-z):
        if char.isalpha():
            # Shift the letter by adding the shift value to its ASCII code (use the ord function)
            ascii_code = ord(char)
            if char.isupper():
                shifted_ascii = (ascii_code - ord('A') + shift) % 26 + ord('A')
            else:
                shifted_ascii = (ascii_code - ord('a') + shift) % 26 + ord('a')
            # Convert the new ASCII code back to a character (use the chr function)
            shifted_char = chr(shifted_ascii)
            # Add the shifted character to the list
            shifted_chars.append(shifted_char)
        else:
            # If the character is not a letter, add it unchanged to the list
            shifted_chars.append(char)
    # After the loop, join the list into a string and return it  
    return ''.join(shifted_chars) 
# Get user input for the message and shift value  
input_message = input("Enter a message to shift: ")
input_shift = int(input("Enter the shift value (integer): "))
# Call the function with the inputs and display the result
result = shift_string(input_message, input_shift)
print("Shifted message:", result)