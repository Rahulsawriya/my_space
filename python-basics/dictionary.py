#A dictionary is a mutable data type that stores mappings of unique keys to values. Here's a dictionary that stores elements and their atomic numbers.
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print("carbon" in elements) # return True
print(elements.get("dilithium")) # return None if element is not in dict


"""Carbon is in the dictionary, so True is printed. Dilithium isn’t in our dictionary so None is returned by get and then printed. If you expect lookups to sometimes fail, 
get might be a better tool than normal square bracket lookups because errors can crash your program."""
n = elements.get("dilithium")
print(n is None) # return True
print(n is not None) # return False