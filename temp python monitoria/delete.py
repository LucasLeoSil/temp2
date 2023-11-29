def reverseheapify(heap, i):
    lower = i
    if i!=0:
        p = (i-1)//2
        if heap[p] < heap[i]:
            heap[p], heap[i] = heap[i], heap[p]
            lower = p
            reverseheapify(heap, lower)

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

def deleteheap(heap,valor):
    f = heap.index(valor)
    heap[-1], heap[f] = heap[f], heap[-1]
    last = heap.pop()
    n = len(heap)
    p = (f-1)//2
    if f!=0 and heap[p]<heap[f]:   
        reverseheapify(heap, f)
    else:
        heapify(heap,n,f)


arr = [100,10,50,3,4,46,49]
deleteheap(arr, 4)
print(arr)
arr = [100,10,50,5,4,46,49,3]
deleteheap(arr,50)
print(arr)