# Import required modules
import time
import string
import random

# Display a welcome message
print("Welcome, to the PassGener!\n")

# Define valid options for user input
valid_options = ["1", "2"]

# Create a loop to receive user requests
while True:
    # Display the menu for password options
    print("- Please select one of the options")
    print("\t1. Create an alphanumeric password.")
    print("\t2. Create a numeric password.")
    # Get the user's choice
    choice = input("\tYour choice: ")

    # Check if the user's choice is valid or not
    if choice not in valid_options:
        print('\n ', '-' * 82)
        print(
            "  Error!\n  Please choose between option 1 or 2.")
        print(' ', '-' * 82, '\n')
        time.sleep(1)
    else:
        if choice == "1":
            while True:
                # Get the desired password length from the user
                pass_len1 = int(input("\nPlease enter the number of characters in your password: "))
                if pass_len1 <= 0:
                    print('\n ', '-' * 82)
                    print(
                        "  Error!\n  The entered value for the password is not correct, please enter a positive number.")
                    print(' ', '-' * 82, '\n')
                    time.sleep(1)
                else:
                    # Define the character set for the alphanumeric password
                    characters = string.ascii_letters + string.digits + string.punctuation
                    # Generate the alphanumeric password
                    password = ''.join(random.choice(characters) for _ in range(pass_len1))
                    # Display the generated password
                    print("Your password is: ", password)
                    break
        elif choice == "2":
            while True:
                # Get the desired password length from the user
                pass_len2 = int(input("\nPlease enter the number of characters in your password: "))
                if pass_len2 <= 0:
                    print('\n', '-' * 82)
                    print("Error!\nThe entered value for the password is not correct, please enter a positive number.")
                    print(' ', '-' * 82, '\n')
                    time.sleep(1)
                else:
                    # Generate the numeric password
                    random.seed(time.time())
                    password = ""
                    for _ in range(pass_len2):
                        numeric = random.randint(0, 9)
                        password += str(numeric)
                    # Display the generated password
                    print("Your password is: ", password)
                    break
        break
