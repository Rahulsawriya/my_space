#pickling is a way to convert a python object (list, dict, etc.) into a character stream.
#python pickle module is used for serializing and de-serializing a Python object structure
import pickle
#pickle the python object
cars = ['Audi', 'BMW', 'Maruti suzuki', 'Toyota']
file = 'mycar.pkl'
fileobj = open(file, 'wb')
pickle.dump(cars, fileobj)
fileobj.close()