def is_palindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True
    else:
        return False

palins = []
nums = []
for numA in range(100,1000):
    for numB in range(100,1000):
        product = numA*numB
        if is_palindrome(product):
            palins.append(product)
            nums.append((numA,numB))
print(nums)
print(palins)
print(max(palins))
