#Lambda functions are mainly used in combination with the functions filter(), map() and reduce().
#These functions are called anonymous because they are not declared in the standard manner by using the def keyword. You can use the lambda keyword to create small anonymous functions.
sum = lambda arg1, arg2 : arg1 + arg2
print("total", sum(10, 20))
