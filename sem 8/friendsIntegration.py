
from random import randint

def getFriends(dict , person):
    friend_list = {}
    for other in dict:
        if other != person:
            x = randint(0,9)
            if x %2 == 0:
                friend_list[other] = 1
            else:
                friend_list[other] = 0

    return friend_list


