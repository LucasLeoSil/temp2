import random

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1 
    r = 2 * i + 2 
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
 
        heapify(arr, n, largest)
        
def createheap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    return arr
 
def heapSort(arr):
    var = createheap(arr)
    n = len(var)
    for i in range(n - 1, 0, -1):
        (var[i], var[0]) = (var[0], var[i]) 
        heapify(arr, i, 0)
    return var

def reverseheapify(heap, i):
    lower = i
    if i!=0:
        p = (i-1)//2
        if heap[p] < heap[i]:
            heap[p], heap[i] = heap[i], heap[p]
            lower = p
            reverseheapify(heap, lower)

def insertheap(heap, valor):
    heap.append(valor)
    n = len(heap)-1
    reverseheapify(heap, n)
     
def deleteheap(heap,valor):
    n = len(heap)-1
    p = heap.index(valor)
    heap[n], heap[p] = heap[p], heap[n]
    last = heap.pop()
    reverseheapify(heap, p)

  

heap = [15,34,56,45,67,76,97,12,66,23,65,87,50,10,90,78]
createheap(heap)
insertheap(heap, 100)
insertheap(heap,33)
insertheap(heap,200)
insertheap(heap, 24)
deleteheap(heap, 66)
deleteheap(heap, 56)
deleteheap(heap, 45)
heapSort(heap)
print(heap)