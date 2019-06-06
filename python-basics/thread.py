"""Thread is basically a lightweight sub-process, a smallest unit of processing.

Multithreading is a process of executing multiple threads simultaneously.

Green thread: green threads are threads that are scheduled by a runtime library or virtual machine (VM) instead of natively by the underlying operating system.

The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter. This means that only one thread can be in a state of execution at any point in time.

GIL allows only one thread to execute at a time even in a multi-threaded architecture """

#lets take an example print square and cube of every number.
import time
import threading
def calc_square(numbers):
	print("calculate square of numbers")
	for n in numbers:
		time.sleep(0.2)
		print(n * n)

def calc_cube(numbers):
	print("calculate cube of numbers")
	for n in numbers:
		time.sleep(0.2)
		print(n * n * n)


arr = [2, 3, 4, 5, 6]
t = time.time()
#calc_square(arr)
#calc_cube(arr)
t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()
print("done in :", time.time()-t)
