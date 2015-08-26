#! /usr/bin/python

import unittest

def chop (target, intarray):
	first = 0
	last = len(intarray) - 1
	found = -1

	while first <= last and found == -1:
		mid = (first + last) // 2 
		if intarray[mid] == target:
			found = mid
		else:
			if target < intarray[mid]:
				last = mid - 1
			else:
				first = mid + 1
	return found

def chop2 (target, intarray, low = 0, high = None):

	if len(intarray) == 0:
		return -1
	if intarray[0] == target:
		return 0

	high = len(intarray) if high is None else high
	pos = low + (high - low) / len(intarray)

	if pos == len(intarray):
		return -1
	elif intarray[pos] == target:
		return pos
	elif high == low:
		return -1 
	elif intarray[pos] < target: 
		return chop2(target, intarray, pos + 1, high)
	else:
		return chop2(target, intarray, low, pos)


class testingkata02(unittest.TestCase):


	def setUp(self):
		pass

	def test_chop_empty(self):
		self.assertEqual(-1, chop(3, []))

	def test_chop_one_term(self):
		self.assertEqual(-1, chop(3, [1]))
		self.assertEqual(0,  chop(1, [1]))

	def test_chop_three_terms(self):		
		self.assertEqual(0,  chop(1, [1, 3, 5]))
		self.assertEqual(1,  chop(3, [1, 3, 5]))
		self.assertEqual(2,  chop(5, [1, 3, 5]))
		self.assertEqual(-1, chop(0, [1, 3, 5]))
		self.assertEqual(-1, chop(2, [1, 3, 5]))
		self.assertEqual(-1, chop(4, [1, 3, 5]))
		self.assertEqual(-1, chop(6, [1, 3, 5]))

	def test_chop_four_terms(self):				
		self.assertEqual(0,  chop(1, [1, 3, 5, 7]))
		self.assertEqual(1,  chop(3, [1, 3, 5, 7]))
		self.assertEqual(2,  chop(5, [1, 3, 5, 7]))
		self.assertEqual(3,  chop(7, [1, 3, 5, 7]))
		self.assertEqual(-1, chop(0, [1, 3, 5, 7]))
		self.assertEqual(-1, chop(2, [1, 3, 5, 7]))
		self.assertEqual(-1, chop(4, [1, 3, 5, 7]))
		self.assertEqual(-1, chop(6, [1, 3, 5, 7]))
		self.assertEqual(-1, chop(8, [1, 3, 5, 7]))

	def test_chop2_empty(self):
		self.assertEqual(-1, chop2(3, []))

	def test_chop2_one_term(self):
		self.assertEqual(-1, chop2(3, [1]))
		self.assertEqual(0,  chop2(1, [1]))

	def test_chop2_three_terms(self):
		self.assertEqual(0,  chop2(1, [1, 3, 5]))
		self.assertEqual(1,  chop2(3, [1, 3, 5]))
		self.assertEqual(2,  chop2(5, [1, 3, 5]))
		self.assertEqual(-1, chop2(0, [1, 3, 5]))
		self.assertEqual(-1, chop2(2, [1, 3, 5]))
		self.assertEqual(-1, chop2(4, [1, 3, 5]))
		self.assertEqual(-1, chop2(6, [1, 3, 5]))

	def test_chop2_four_terms(self):
		self.assertEqual(0,  chop2(1, [1, 3, 5, 7]))
		self.assertEqual(1,  chop2(3, [1, 3, 5, 7]))
		self.assertEqual(2,  chop2(5, [1, 3, 5, 7]))
		self.assertEqual(3,  chop2(7, [1, 3, 5, 7]))
		self.assertEqual(-1, chop2(0, [1, 3, 5, 7]))
		self.assertEqual(-1, chop2(2, [1, 3, 5, 7]))
		self.assertEqual(-1, chop2(4, [1, 3, 5, 7]))
		self.assertEqual(-1, chop2(6, [1, 3, 5, 7]))
		self.assertEqual(-1, chop2(8, [1, 3, 5, 7]))

	def test_chop2_five_terms(self):
		self.assertEqual(0,  chop2(1, [1, 3, 5, 7, 9]))
		self.assertEqual(3,  chop2(7, [1, 3, 5, 7, 9]))
		self.assertEqual(4,  chop2(9, [1, 3, 5, 7, 9]))

	def test_chop2_twelve_terms(self):
		self.assertEqual(-1,  chop2(8, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]))
		self.assertEqual(9,  chop2(19, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]))
		self.assertEqual(1,  chop2(3, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]))


if __name__ == '__main__':
	unittest.main()
