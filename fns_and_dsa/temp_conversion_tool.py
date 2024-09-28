# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Factor for Fahrenheit to Celsius conversion
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Factor for Celsius to Fahrenheit conversion

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # User input for temperature and scale
        temperature = float(input("Enter the temperature to convert: "))
        scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Check which conversion function to call based on the input scale
        if scale == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {converted_temp:.1f}°F")
        elif scale == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {converted_temp:.2f}°C")
        else:
            print("Invalid input. Please specify 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
