# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats for division
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Attempt to divide
        result = numerator / denominator
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."

