import datetime

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format to "YYYY-MM-DD HH:MM:SS"
    print(f"Current Date and Time: {formatted_date}")
    return current_date  # Returning for potential use in other functions

# Part 2: Calculate a Future Date
def calculate_future_date(days):
    current_date = display_current_datetime()  # Get the current date from the function
    future_date = current_date + datetime.timedelta(days=days)  # Add the specified number of days
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date to "YYYY-MM-DD"
    print(f"Future Date after {days} days: {formatted_future_date}")

def main():
    display_current_datetime()  # Display the current date and time

    # Prompt the user for the number of days to add
    try:
        days_to_add = int(input("Enter the number of days to calculate the future date: "))
        calculate_future_date(days_to_add)
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()

