a = int(input())
letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "l", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

string = input()


string = list(string.lower())

s = "YES"
if len(string) < 26:
    s = "NO"
else:
    for i in range(len(letter)):
        if letter[i] not in string:
            s = "NO"
            break

print(s)
