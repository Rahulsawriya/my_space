"""xrange and range are the exact same in terms of functionality. They both provide a way to generate a list of integers for you to use, however you please. The only difference is that range returns a Python list object and xrange returns an xrange object.

What does that mean? Good question! It means that xrange doesn't actually generate a static list at run-time like range does. It creates the values as you need them with a special technique called yielding."""

print(range(0, 20))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print(xrange(0, 20))
#xrange(20)


"""In Python 3, there is no xrange , but the range function behaves like xrange in Python 2.If you want to write code that will run on both Python 2 and Python 3, you should use range(). range() – This returns a list of numbers created using range() function."""
