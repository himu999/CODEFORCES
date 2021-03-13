t = int(input())
a = list(map(int, input().split()))
summation = ((sum(a) / 100) / t) * 100

print("{:.12f}".format(summation))
