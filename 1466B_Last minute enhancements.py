t = int(input())

while t > 0:
    n = int(input())
    a = map(int, input().split())
    a = list(a)
    st = set()

    for i in range(n):
        if a[i] in st:
            st.add(a[i] + 1)
        else:
            st.add(a[i])
    print(len(st))

    t -= 1
