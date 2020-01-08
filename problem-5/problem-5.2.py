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


while True:
    number+=20
    if check(number):
        break
    print(number)

print('este:')
print(number)


