"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes < 1:
        raise ValueError("Value entered must be larger than 1.")

    total = 0
    start = 2
    numbers = 0

    while total < number_of_primes:

        numbers = 0

        if start == 2:
            list.append(start)
            start+=1
            total+=1
            continue

        for x in range(1, start+1):
            if(start % x == 0):
                numbers+=1
        
        if numbers == 2:
            list.append(start)
            start+=1
            total+=1
        else:
            start+=1

    return list


    
