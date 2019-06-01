#closures: its a nested function where nested functions can access the variable of the enclosing scope.
def gen_multiplier(x):
    def multiplier(y):
        return x * y
    return multiplier
m = gen_multiplier(10)
print(m(5))
