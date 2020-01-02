def sum_of_multiples(number):
    numbers=[]
    for i in range(0,number):
        if i%5==0 or i%3==0:
            numbers.append(i)
    return sum(numbers)

print(sum_of_multiples(1000))

