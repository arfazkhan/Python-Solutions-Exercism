def steps(number):
    # Check if the input is a positive integer
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    # Initialize the step counter
    step_count = 0
    
    # Apply the Collatz Conjecture until the number becomes 1
    while number != 1:
        if number % 2 == 0:
            number //= 2  # Divide by 2 if even
        else:
            number = 3 * number + 1  # Multiply by 3 and add 1 if odd
        step_count += 1  # Increment the step counter
    
    return step_count
