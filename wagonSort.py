import os
import random

os.system('clear')
''' Define the road capacities '''
road1 = 5
road2 = 3
road3 = 2

''' Set up the freight stock wagons '''
wagonList1 = ['2399', '45001', '1334', '45887', '89989', '5823', '12339',
              '87612', '47660', '7772']
wagonList2 = wagonList1

''' Define function to select random wagon numbers '''


def listSelection(road, wagonList2):
    for _ in range(road):
        selection = str(random.choice(wagonList2))
        print(_, ':', selection)
        wagonList2.remove(selection)
    return wagonList2


''' Main program '''


def main():
    print('Wagons placed in spur 1: ')
    road = road1
    listSelection(road, wagonList2)

    print('Wagons placed in spur 2: ')
    road = road2
    listSelection(road, wagonList2)

    print('Wagons placed in spur 3: ')
    road = road3
    listSelection(road, wagonList2)


main()
