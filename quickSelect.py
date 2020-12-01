# Quick Select algorithm
def partition(list,l,r):
    y = list[r]
    x = l
    # Partition procedure.
    # Move smaller values of pivot to the left of the pivot
    for i in range(l,r):
        if (list[i] <= y):
            list[x], list[i] = list[i], list[x]
            x += 1

    list[x], list[r] = list[r], list[x]
    return x

def QS(list,l,r,k):
    if (k > 0 and k <= r-l+1): # Ensure k is a value within the allowable range
        index = partition(list,l,r)

        if (index-l == k-1): # if index is k, return the value
            return list[index]

        if (index-l > k-1): # if index is above k, check left subarray
            return QS(list,l,index-1,k)

        return QS(list,index+1,r,k-index+l-1) # if index is below k, check right subarray

    return "Hmmmmmmmmmm"

def quick_select(k,list):
    n = len(list)
    return QS(list,0,n-1,k)

# Main
# generate random integer values
from random import seed
from random import randint
from datetime import datetime
from timeit import default_timer as timer

# seed random number generator
d = datetime.now()
seed(d)
list = []
# generate some integers
for i in range(10000):
	arr.append(randint(0, 50000))
print("K-th smallest element is ", end = "")
print(quick_select(200,list))
