import threading

def merge(first, mid , last):
    left = A[first:mid+1]+[float('inf')]
    right = A[mid+1:last+1]+[float('inf')]

    i = 0
    j = 0

    for k in range(first, last+1):
        if left[i] <= right[j]:
            A[k] = left[i]
            i+=1
        else:
            A[k] = right[j]
            j+=1
    

def mergeSort(first, last):
    mid = (first + last)//2
    if first < last:
        mergeSort(first, mid)
        mergeSort(mid+1, last)
        merge(first, mid, last)

def mergeSortThread(i):
    size = length//4 
    first = i * size
    last = (i*size+size)-1
    mid = (first + last)//2
    if first < last:
        mergeSort(first, mid)
        mergeSort(mid+1, last)
        merge(first, mid, last)
    


A = [5,4,3,2,1,6,0,9,8,7,12,11]
print(A)
length = len(A)

threads = []
for i in range(4):
    threads.append(threading.Thread(target = mergeSortThread, args = (i,)))
    
for i in range(4):
    threads[i].start()


for i in range(4):
    threads[i].join()

merge(0,(length//2-1)//2 ,length//2-1)
merge(length//2, length//2 + ((length-1) - length//2)//2, length-1)
merge(0, (length-1)//2, length-1)

print(A)
