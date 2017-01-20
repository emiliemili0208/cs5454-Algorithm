import datetime
import random
import matplotlib.pyplot as plt
import time
import timeit


arr = []
for i in range(0, 10): 
	arr.append(i)
#print arr

def root(i):
    a = i
    while(a != arr[a]):
        a = arr[a]
    return a

def find(a,b):
    if root(a) == root(b):
        #print("YES")
        #print root(a)
        return True
    else:
        #print("NO")
        return False

def union(a,b):
    aid = root(a)
    bid = root(b)
    arr[aid] = root(bid)

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