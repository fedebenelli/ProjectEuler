# Code by lassevk - Thu, 22 Sep 2005, 12:06

i = 1
for k in range(1, 21):
    for j in range(1, 21):
        if (i*j) % k == 0:
            i *= j
            break
print(i)
