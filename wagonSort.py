import os
import random

os.system('clear')

road1 = 5
road2 = 3
road3 = 2

wagonList1 = ['8990', '1234', '6424', '9000', '6565', '34104', '19233', '2944', '77699', '6001', '55677']
wagonList2 = wagonList1

def listSelection(road, wagonList2):
    for _ in range(road):
        selection = str(random.choice(wagonList2))
        print(_, ':', selection)
        wagonList2.remove(selection)
    return wagonList2

road = road1
listSelection(road, wagonList2)
a = (len(wagonList2))
print('Length of wagonList2 left: ', a)

road = road2
listSelection(road, wagonList2)
a = (len(wagonList2))
print('Length of wagonList2 left: ', a)

road = road3
listSelection(road, wagonList2)
a = (len(wagonList2))
print('Length of wagonList2 left: ', a)
