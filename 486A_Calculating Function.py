n = int(input())
summation = 1

if n % 2 == 0:
    b = n // 2
    summation *= b

elif n % 2 != 0 and n > 1:
    b = (n-1) // 2
    summation = (summation * b) - n
else:
    summation = -1

print(summation)
