# daily_reminder.py

def main():
    # Prompt for task description
    task = input("Enter your task: ")

    # Prompt for task priority
    priority = input("Priority (high/medium/low): ").lower()

    # Ask if the task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Initialize the reminder message
    reminder = f"'{task}' is a "

    # Use match case to determine priority
    match priority:
        case "high":
            reminder += "high priority task"
        case "medium":
            reminder += "medium priority task"
        case "low":
            reminder += "low priority task"
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")
            return

    # Check if the task is time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    # Print the customized reminder
    print("\nReminder:", reminder)

if __name__ == "__main__":
    main()
