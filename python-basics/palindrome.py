class Number():
	def palindrome(self, num):
		temp = num
		final = 0
		while (num != 0):
			rem = num % 10
			final = final * 10 + rem
			num = num // 10
		if (final == temp):
			print("Number is a palindrome")
		else:
			print("number is not palindrome")
obj = Number()
obj.palindrome(121)


'''
308
down vote
accepted
In Python 3.0, 5 / 2 will return 2.5 and 5 // 2 will return 2. The former is floating point division, and the latter is floor division, sometimes also called integer division.

In Python 2.2 or later in the 2.x line, there is no difference for integers unless you perform a from __future__ import division, which causes Python 2.x to adopt the behavior of 3.0

Regardless of the future import, 5.0 // 2 will return 2.0 since that's the floor division result of the operation. 

'''
