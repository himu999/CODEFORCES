number1, number2 = map(int, input().split())

i = 1

while i <= number2:

    if number1 % 10 == 0:
        number1 = number1 // 10

    else:

        number1 = number1 - 1

    i = i + 1

print(number1)
