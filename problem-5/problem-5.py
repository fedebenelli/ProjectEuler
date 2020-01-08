number=20
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def get_number(numbers):
    new_number = 1
    for number in numbers:
        if number != 0:
            new_number *= number

    return new_number

def check(number):
    for i in range(1,21):
        if number%i != 0:
            return False
    return True

def new_numbers(IL, SL, prev_number):
    new_number = [0]*20
    
    for i in range(IL, SL):
        new_number[i] = prev_number[i]
    return new_number

combinations = []

for IL in range(0,21):
    for SL in range(0,21):
        if IL<SL:
            combinations.append(new_numbers(IL,SL,numbers))
multiples = []
for combination in combinations:
    print(combination)
    print(get_number(combination))
    if check(get_number(combination)):
        multiples.append(get_number(combination))
print(multiples)
print(min(multiples))
