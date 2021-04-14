n = int(input())
lst = map(int, input().split())
lst = list(lst)
cont = 1
memory = 1

for i in range(n-1):
    if lst[i] < lst[i+1]:
        cont += 1

        if memory < cont:
            memory = cont
    else:
        cont = 1

print(memory)
