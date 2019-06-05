#unpickling is the inverse operation, whereby a character stream is converted back into an object hierarchy.
import pickle
#unpickling the python object
file = "mycar.pkl"
fileobj = open(file, 'rb')
print(pickle.load(fileobj))
fileobj.close()