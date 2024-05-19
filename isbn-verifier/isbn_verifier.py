def is_valid(isbn):
    # Remove hyphens
    isbn = isbn.replace('-', '')
    
    # Check length
    if len(isbn) != 10:
        return False
    
    # Initialize the checksum
    checksum = 0
    
    # Loop through each character
    for i, char in enumerate(isbn):
        if char == 'X':
            # 'X' can only be the last character
            if i == 9:
                value = 10
            else:
                return False
        elif char.isdigit():
            value = int(char)
        else:
            return False
        
        checksum += value * (10 - i)
    
    # The checksum should be divisible by 11
    return checksum % 11 == 0
