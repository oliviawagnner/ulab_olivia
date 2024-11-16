import numpy as np  # Import numpy to run operations

def number_selection(arr):  # Take all the elements of the array, and if they are less than or equal to 5, return it as a list
    selected_numbers = []  # Selected numbers of array (defined in jupyter notebook)
    for num in arr.flatten():  # For loop
        if num <= 3:
            selected_numbers.append(num)
    return selected_numbers  # Retrn the numbers that are less than or equal to 5

def sum_numbers(numbers):  # Take the values in the list from above, adds them by group
    numbers = np.array(numbers).flatten()  # Defines numbers as the list from above
    sum_even = np.sum(num for num in numbers if num % 2 == 0)  # Sum of all even numbers
    sum_odd = np.sum(num for num in numbers if num % 2 != 0)  # Sum of all odd numbers
    sum_even_odd = np.sum(numbers)  # Sum of all numbers
    
    a = sum_even  # Defines a as sum_even
    b = sum_even_odd  # Defines b as sum_even_odd
    c = sum_odd  # Defines c as sum_odd

    return a, b, c  # Return a, b, c, to use in nexdt part

def quadratic_roots(a, b, c):  # Perform quadratic formula with a, b, c, from above
    discriminant = b ** 2 - 4 * a  *c  # Define discriminat to split into 3 categories: 2 real roots, 1 real root, 2 imaginary roots
    
    if discriminant > 0:  # If statement for 2 real roots
        root1 = (-b + ((discriminant) ** 1/2)) / (2 * a)
        root2 = (-b - ((discriminant) ** 1/2)) / (2 * a)
        return (root1, root2)
    elif discriminant == 0:  # Elif statement for 1 real root
        root = -b / (2 * a)  # Where discriminat is 0
        return (root,)
    else:  # Else statement for 2 imaginary roots
        realPart = -b / (2 * a) 
        imaginaryPart = ((-discriminant) ** 1/2) / (2 * a)
        return (realPart + imaginaryPart * 1j, realPart - imaginaryPart * 1j)  # Sets up the 