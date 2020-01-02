def is_prime(number):
    
    if number == 0:
        return False
    
    elif number == 1:
        return False 
    
    for i in range(2, number):
        if number%i == 0:
            return False

    return True

def get_factors(number):
    factors=[]
    for i in range(2,number):
        if number%i == 0:
            factors.append(i)
    return factors


number = 600851475143
primes = []
factors = get_factors(number)
for i in factors:    
    if is_prime(i):
        primes.append(i)

print(primes)
print(f'The biggest prime factor is: {primes[-1]}')
