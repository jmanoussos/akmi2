def calculator():
    print("Welcome to the Python Calculator!")
    print("Options:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    try:
        # Get user input for the operation
        choice = input("Enter the number for the operation (1/2/3/4): ").strip()

        # Validate choice
        if choice not in ('1', '2', '3', '4'):
            print("Invalid option. Please restart the calculator.")
            return

        # Get numbers for the calculation
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the chosen operation
        if choice == '1':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result}.")
        elif choice == '2':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result}.")
        elif choice == '3':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is {result}.")
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is {result}.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values only.")

# Run the calculator
if __name__ == "__main__":
    calculator()
