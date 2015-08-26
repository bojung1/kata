#! /usr/bin/python

#thinking about this, it seems like I have to determine the following:
#1. Where is the middle of the array? 
#2. How do I determine the next slice of the array to scan?
#3. How do I determine the middle of THAT array? 
#4. Seems like we will be using a list in python. 

class kata02chop:
	def chop (target, intarray):
		listcount=len(intarray)
		if listcount == 0:
			return -1
		elif listcount == 1:
			if intarray[0]==target:
				return 0
			else:
				return -1
#		else
#			if listcount%2 == 0:


def __init__(self):
	self.data = []

	