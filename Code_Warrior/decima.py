# DESCRIPTION:

# Each number should be formatted that it is rounded to two decimal places. You don't need to check whether the input is a valid number because only valid numbers are used in the tests.

# Example:    
# 5.5589 is rounded 5.56   
# 3.3424 is rounded 3.34

#Option 1

def round_to_two_decimal_places(number):
    # Step 1: Multiply the number by 100
    multiplied = number * 100
    
    # Step 2: Add 0.5 to the result
    added = multiplied + 0.5
    
    # Step 3: Convert the result to an integer (truncate the decimal part)
    truncated = int(added)
    
    # Step 4: Divide by 100 to get the result rounded to two decimal places
    rounded = truncated / 100
    
    return rounded

# Test cases
print(round_to_two_decimal_places(5.5589))  # Output: 5.56
print(round_to_two_decimal_places(3.3424))  # Output: 3.34


#Option 2
 
def round_to_two_decimal_places(number):
    # Convert the number to an integer with the desired precision
    scaled_number = int(number * 1000)
    
    # Extract the part corresponding to two decimal places and the extra digit for rounding
    two_decimal_part = scaled_number // 10
    extra_digit = scaled_number % 10
    
    # Perform rounding
    if extra_digit >= 5:
        two_decimal_part += 1
    
    # Convert back to a float with two decimal places
    result = two_decimal_part / 100.0
    
    return result

# Test cases
print(round_to_two_decimal_places(5.5589))  # Output: 5.56
print(round_to_two_decimal_places(3.3424))  # Output: 3.34

#Option3

n = 5.5589
print(n/1.00)

def two_decimal_places(n):
    raise NotImplementedError("TODO: two_decimal_places")