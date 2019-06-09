#try() is used in Error and Exception Handling.
"""List of Exception Errors :

IOError : if file can’t be opened
KeyboardInterrupt : when an unrequired key is pressed by the user
ValueError : when built-in function receives a wrong argument
EOFError : if End-Of-File is hit without reading any data
ImportError : if it is unable to find the module"""

def divide(x, y):
	try: 
	# Floor Division : Gives only Fractional Part as Answer 
		result = x // y
		print("Yeah ! Your answer is :", result)
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")
	finally:
		print("The 'try except' is finished") 
  
# Look at parameters and note the working of Program 
divide(3, 0) 
