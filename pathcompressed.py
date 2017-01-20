import datetime
import random
import matplotlib.pyplot as plt
import time
import timeit

arr = []
for i in range(0, 10): 
	arr.append(i)
#print arr

sz = []
for i in range(0, len(arr)): 
    sz.append(1)


def root(i):
    a = i
    while(arr[a] != a):
        arr[a] = arr[arr[a]]
        a = arr[a]
    return a

def find(a,b):
    if root(a) == root(b):
        arr[a]=arr[root(a)]
        #print("YES")
        #print root(a)
        #print root(b)
        return True
    else:
        #print("NO")
        return False

def union(a,b):
    if sz[root(a)] > sz[root(b)]:
        sz[root(a)] += sz[root(b)]
        arr[root(b)] = root(a)
    else:
        sz[root(b)] += sz[root(a)]
        arr[root(a)] = root(b)
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
    timetotal.append((stop-start)/j)
    for p in range(0, 1000): 
        arr.append(p)
print timetotal


