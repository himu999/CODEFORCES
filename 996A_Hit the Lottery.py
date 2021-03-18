a = int(input())

b = [1, 5, 10, 20, 100]
cont = 0
for i in range(len(b)-1, -1, -1):

    while a >= b[i] and a != 0:

        summ = a // b[i]
        a = a - (summ * b[i])
        cont += summ

print(cont)
