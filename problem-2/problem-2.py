def fibonacci(last_pos):
    fib_list = []
    for i in range(1, last_pos+1):
        if i > 2:
            fib_list.append(fib_list[-1] + fib_list[-2])
        elif i==1:
            fib_list.append(i)
        elif i==2:
            fib_list.append(i)
    return fib_list

def sum_even(numbers):
    sum=0
    for number in numbers:
        if number%2==0:
            sum+=number
    return sum


count = 2 
fib_list = fibonacci(count)

while fib_list[-1]+fib_list[-2] < 4000000:
    fib_list = fibonacci(count)
    sum = sum_even(fib_list)
    count += 1
    print(sum)

print(fib_list)

