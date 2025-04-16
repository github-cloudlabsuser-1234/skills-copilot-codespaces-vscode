def calculator():
    """
    A simple calculator function that allows the user to perform basic arithmetic operations.

    The user can select from the following operations:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Percentage

    The function prompts the user to input their choice of operation and the required numbers.
    It performs the selected operation and displays the result.

    Error Handling:
    - Ensures that the user inputs valid numbers.
    - Handles division by zero gracefully by displaying an error message.
    - Validates the user's choice of operation and prompts for a valid input if necessary.

    Returns:
        None
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4', '5']:
        try:
            num1 = float(input("Enter first number: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            try:
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Please enter a valid number.")
                return
        if choice == '5':
            print(f"The result is: {num1 / 100}")
        else:
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result is: {num1 + num2}")
            elif choice == '2':
                print(f"The result is: {num1 - num2}")
            elif choice == '3':
                print(f"The result is: {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"The result is: {num1 / num2}")
                else:
                    print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input. Please select a valid operation.")

if __name__ == "__main__":
    calculator()
