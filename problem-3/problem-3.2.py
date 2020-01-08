from math import sqrt

def is_prime(number):
    
    if number == 0:
        return False
    
    elif number == 1:
        return False 
    i = 3
    while i*i < number:
        print(i)
        if number%i == 0:
            return False
        i+=2

    return True

def get_factors(number):
    factors=[]
    for i in range(2,number):
        if number%i == 0:
            factors.append(i)
    return factors


number = 600851475143
primes = []
factors = []

for i in range(2,number):
    if number%i == 0:
        number=int(number/i)
        break


for i in range(number,0,-1):
    if number%i==0:
       if is_prime(i):
           print(f'the biggest prime factor is: {i}')
           break
