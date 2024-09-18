# match_case_calculator.py

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def perform_operation(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 == 0:
                return "Cannot divide by zero."
            return num1 / num2
        case _:
            return "Invalid operation selected."

def main():
    # Get user input for numbers
    num1 = get_number_input("Enter the first number: ")
    num2 = get_number_input("Enter the second number: ")

    # Get user input for operation
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform the operation using match-case
    result = perform_operation(num1, num2, operation)

    # Output the result
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
