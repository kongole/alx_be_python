# pattern_drawing.py

def main():
    # Prompt the user for the pattern size
    size = int(input("Enter the size of the pattern: "))

    # Ensure the input is a positive integer
    if size <= 0:
        print("Please enter a positive integer.")
        return

    # Use a while loop for each row
    row = 0
    while row < size:
        # Use a for loop to print asterisks in each row
        for _ in range(size):
            print("*", end="")

        # Print a newline character after each row
        print()

        # Increment the row counter
        row += 1

if __name__ == "__main__":
    main()
