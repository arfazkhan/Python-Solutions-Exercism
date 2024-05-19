def is_armstrong_number(number):
    # Convert the number to a string to count the number of digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the sum of the digits raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum equals the original number
    return armstrong_sum == number