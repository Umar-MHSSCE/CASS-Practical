# Umar Farooque (221208)
# PROGRAM TO IMPLEMENT AFFINE CIPHER

#Import required modules
import random
import math
import string

# Mapping letters to numbers (A=0, B=1, ..., Z=25)
charDict = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
    "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19,
    "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25
}

# Reverse mapping (numbers back to letters)
inverseDict = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
    20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'
}

# Function to generate a valid key k1 (must be coprime with 26)
def generateK1():
    while True:
        num = random.randint(1, 26)  # Random number between 1 and 26
        if math.gcd(num, 26) == 1:  # Check if the number is coprime with 26
            return num

# Generate keys k1 and k2
k1 = generateK1()
k2 = random.randint(1, 26)  # Random number for k2 between 1 and 26

# Main loop to either encrypt or decrypt messages
while True:
    choice = input("Press- \n 1. Encryption || 2. Decryption || 3. Exit\n")

    # Encryption option
    if choice == "1":

        # Get the message from the user and format it
        message = input("Enter your message: ").upper()  # Convert message to uppercase
        # Removing spaces and punctuation
        message = message.replace(" ", "")  # Remove spaces
        message = message.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation

        # Write the formatted message to a file
        f = open("file.txt", "w")
        f.write(message)
        f.close()

        print("Formatted message before encryption:", message)

        cipher = ""  # Initialize an empty string for the cipher text

        # Encrypt the message using Affine cipher
        for i in message:
            m = charDict[i]  # Convert letter to number
            c = ((k1 * m) + k2) % 26  # Apply the Affine cipher formula
            number = inverseDict[c]  # Convert the number back to letter
            cipher += number  # Add the letter to the cipher text

        # Write the cipher text to a file
        f = open("file.txt", "w")
        f.write(cipher)
        f.close()

        print("Cipher text:", cipher)
        print("key 1:", k1)  # Display the keys used
        print("key 2:", k2)

    # Decryption option
    elif choice == "2":
        choice2 = input("Press 1 to decrypt cipher text from the file \nPress 2 to decrypt your cipher text\n ")

        plaintext = ""  # Initialize an empty string for the decrypted message

        # Function to find the modular inverse of k1
        def k_inverse(k):
            for i in range(26):
                if (k * i) % 26 == 1:  # Check if it's the modular inverse
                    return i

        # Decrypting from file
        if choice2 == "1":
            f = open("file.txt", "r")  # Open file to read the cipher text
            f.seek(0)
            cipher = f.read()  # Read the entire content
            f.close()

            k1inv = k_inverse(k1)  # Get the modular inverse of k1

            # Decrypt the cipher text using the inverse of k1 and k2
            for i in cipher:
                c = charDict[i]  # Convert letter to number
                m = (k1inv * (c - k2)) % 26  # Apply the decryption formula
                number = inverseDict[m]  # Convert the number back to letter
                plaintext += number  # Add the letter to the decrypted message

            # Write the plaintext to the file
            f = open("file.txt", "w")
            f.write(plaintext)
            f.close()

            print("Plain text:", plaintext)

        # Decrypting user inputted cipher text
        elif choice2 == "2":
            cipher = input("Enter your cipher text: ").upper()  # Take cipher text from user
            key1 = int(input("Enter the value of key 1: "))  # Take key 1 from user
            key2 = int(input("Enter the value of key 2: "))  # Take key 2 from user

            key1inv = k_inverse(key1)  # Get the modular inverse of the entered key 1

            # Decrypt the cipher text using the inverse of key1 and key2
            for i in cipher:
                c = charDict[i]  # Convert letter to number
                m = (key1inv * (c - key2)) % 26  # Apply the decryption formula
                number = inverseDict[m]  # Convert the number back to letter
                plaintext += number  # Add the letter to the decrypted message

            # Write the plaintext to the file
            f = open("file.txt", "w")
            f.write(plaintext)
            f.close()

            print("Plain text:", plaintext)

        else:
            print("Invalid input")  # If an invalid option is selected

    # Exit the program
    else:
        break
