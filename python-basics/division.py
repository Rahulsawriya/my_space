"""In Python 3.0, 5 / 2 will return 2.5 and 5 // 2 will return 2. The former is floating point division, and the latter is floor division, sometimes also called integer division.

In Python 2.2 or later in the 2.x line, there is no difference for integers unless you perform a   , which causes Python 2.x to adopt the behavior of 3.0

Regardless of the future import, 5.0 // 2 will return 2.0 since that's the floor division result of the operation. (from __future__ import division)"""


In python 3.0
5/2 = 2.5
5/2.0 = 2.5
5.0/2 = 2.5
5.0/2.0 = 2.5

In python 2
5/2 = 2
5/2.0 = 2.5
5.0/2 = 2.5
5.0/2.0 = 2.5

In python 3.0
print(5//2) = 2
print(5//2.0) = 2.0
print(5.0//2) = 2.0
print(5.0//2.0) = 2.0

In python 2
print 5//2 = 2
print 5//2.0 = 2.0
print 5.0//2 = 2.0
print 5.0//2.0 = 2.0

