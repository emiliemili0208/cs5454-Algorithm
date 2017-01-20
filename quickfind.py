import datetime
import random
import matplotlib.pyplot as plt
import time
import timeit

arr = []
for i in range(0, 1000): 
	arr.append(i)
#print arr


def find(a,b):
	if arr[a]==arr[b]:
		#print "YES"
		return True
	else:
		#print "NO"
		return False

def union(a,b):
	aid = arr[a]
	bid = arr[b]
	if aid == bid:
		return arr
	for i in range(0,len(arr)):
		if arr[i]== aid:
			arr[i]= bid	
	##print arr
	return arr

timetotal = []
for j in range(10, 1000):
	##start_time = time.time()
	
	#start = timeit.default_timer()
	for i in range(0, j/2): 
		a = random.randint(0,j-1)
		b = random.randint(0,j-1)
		if not find(a,b):
			union(a,b)

	start = timeit.default_timer()
	for i in range(0, j): 
		a = random.randint(0,j-1)
		b = random.randint(0,j-1)
		find(a,b)
		
	stop = timeit.default_timer()
	##timetotal.append((time.time() - start_time)/j)
	timetotal.append((stop-start)/j)
	for p in range(0, 1000): 
		arr.append(p)
print timetotal

