elephant_move = [1, 2, 3, 4, 5]
b = max(elephant_move)
friend_house = int(input())

if friend_house % b == 0:
    print(friend_house // b)
else:
    friend_house = friend_house // b
    print(friend_house + 1)
