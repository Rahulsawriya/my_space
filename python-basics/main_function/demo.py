# demo.py

import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)
print(uf.__name__)

"""To avoid running executable statements in a script when it's imported as a module in another script, include these lines in an if __name__ == "__main__" block. 
Or alternatively, include them in a function called main() and call this in the if main block."""