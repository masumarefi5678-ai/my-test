def is_prime(numbers):
    if numbers > 1:
        for i in range(2, numbers):
            if numbers % i == 0:
                return False
        return True
    return False

def show_primes(start, end):
    for numbers in range(start, end+1):
        if is_prime(numbers):
            print(numbers, end=" ")

show_primes(2, 100)