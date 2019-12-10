# *args allows us to pass variable number of arguments to the function.
def sum(*args):
    s = 0
    for i in args:
        s += i
    print("sum is", s)
sum(2, 3, 4)

#**kwargs allows us to pass variable number of keyword argument like this func_name(name='rahul', age=24)
def my_func(**kwargs):
    for i, j in kwargs.items():
        print(i, j)
my_func(name="rahul", age=24)