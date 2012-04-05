'''
Created on Apr 5, 2012

@author: Rishi Maharaj
'''
def quicksort(A, n, l, r):
    if n <= 1:
        return
    
    p = partition(A, l, r)

    quicksort(A, p-1-l, l, p-1)
    quicksort(A, r-p+1, p, r)
    return A
    
def partition(A, l, r):
    p = A[l]
    i = l+1
    for j in range(l+1,r+1):
        if A[j] < p:
            swap(A,j,i)
            i += 1
    swap(A,l,i-1)
    return i

def swap(A, x, y):
    t = A[x]
    A[x] = A[y]
    A[y] = t

def choosePivot(A,n,offset):
    #pIndex = n/2 + offset
    #if pIndex < 0 or pIndex > n:
    #    
    #for item in seenPivots:
    #    if item == A[pIndex]:
    #        choosePivot
    return offset

print quicksort([3,8,2,5,1,4,7,6], 8, 0, 8-1)
print quicksort([1,2,3,4,5,6,7,8], 8, 0, 8-1)
print quicksort([56,8,4,2567,0,65,2,5,7,8,9567,8,5,7,15,98,31,98,15,89,165,498,15,21,3,9,123,98,123], 29, 0, 29-1)
print quicksort([54044,14108,79294,29649,25260,60660,2995,53777,49689,9083,16122,90436,4615,40660,25675,58943,92904,9900,95588,46120], 20, 0, 20-1)