#Decorators are allowed programmers to modify the behavior of function or class. 
#Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.
def check(func):
  def inside(a, b):
      if b==0:
          print("can't divide by 0")
          return
      func(a, b)
  return inside
@check
def div(a, b):
  return a/b
print(div(10, 0))
