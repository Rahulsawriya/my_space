_a = 1 =>Python doesn't have real private methods, so one underline in the beginning of a method or attribute means you shouldn't access this method, because it's not part of the API. It's very common when using properties:
__a = 1 => This one causes a lot of confusion. It should not be used to mark a method as private, the goal here is to avoid your method to be overridden by a subclass.
__a__ = 1 => When you see a method like __this__, the rule is simple: don't call it. Why? Because it means it's a method python calls, not you.


