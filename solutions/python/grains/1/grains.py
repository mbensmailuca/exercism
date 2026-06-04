def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)
        
        


def total():
    total_value = 0
    for number in range(1, 65):
        total_value += square(number)
    return total_value
