'''This is my first proper python program'''

''' Import Libraries'''
import os
import random #random function for randomly selecting the wagons and industries and spots

'''First set up individual wagon data'''
wagonList = ['PAM2399', 'GUI45001', 'NEC1334', 'GUI45887', 'CSX89989', 'CPR5823', 'PWR12339', 'PAM87612', 'GUI47660', 'NEC7772']

''' Setup road wagon capacities '''
#future upgrade to calculate wagons from inputs
road1 = 5
road2 = 3
road3 = 2

''' Select the random number from 0 to wagonListEnd'''
def randWagGen():
	dic_len = (len(wagonList)-1)
	randNum = random.randint(0, dic_len)
	# print(dic_len)
	return randNum

''' Populate Road 1 with wagons inbound '''
def road1cap(road1):
	print('Road One allows for', road1, 'Unsorted Wagons'	)
	# Call random wagon selection here 
	return

''' Populate Road 2 with wagons outbound '''
def road2cap(road2):
	print('Road One allows for', road2, 'Sorted Wagons') 
	# Call random wagon selection here
	return

''' Populate Road 3 with wagons in spots '''
def road3cap(road3):
	print('Road One allows for', road3, 'Spoted Wagons') 
	# Call random wagon selection here
	return
	

''' Main Program '''
def main():
	#clear the screen
	os.system('clear')
	''' First show road capacities '''
	road1cap(road1)
	road2cap(road2)
	road3cap(road3)
	
	for _ in range(road1):
		road1randNum = randWagGen()
		#IF wagon == previous skip to nextrand num
		wagList1 = wagonList[road1randNum]
		print(wagList1)
		
''' Call main function to run program '''
main()

