# This is a program to calculate the factorial of a given number.
while True:
    # Request a number from the user.
    number = int(input("Please enter a number: "))
    factorial = 1

    # Check if the input number is negative.
    if number < 0:
        print("Factorial is not defined for negative numbers.\n")

    # Check if the input number is 0 or 1.
    elif number == 0 or number == 1:
        print(f"The factorial of {number} is 1.")
        break

    else:
        # Calculate the factorial using a loop for numbers greater than 1.
        for pre_num in range(2, number + 1):
            factorial *= pre_num
        print(f"The factorial of {number} is: {factorial}")
        break