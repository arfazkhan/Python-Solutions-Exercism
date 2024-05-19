def steps(number, memo={}):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    count = 0
    while number != 1:
        if number in memo:
            return count + memo[number]
        if number & 1 == 0:  # faster check for evenness
            number = number >> 1  # bit manipulation for division by 2
        else:
            number = 3 * number + 1
        count += 1
    memo[number] = count
    return count