#multithreading and multiprocessing both are ways to achieve multitasking.
#The benefit of multiprocessing is that error of memory leak in one process won't hurt execution of another process.
import time
import multiprocessing
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
p1 = multiprocessing.Process(target=calc_square, args=(arr,))
p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

p1.start()
p2.start()

p1.join()
p2.join()
print("done in :", time.time()-t)