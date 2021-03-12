string = input()
string1 = input()

cont = 0

if string.lower() < string1.lower():
    print("-1")
elif string.lower() > string1.lower():
    print("1")
else:
    print("0")
