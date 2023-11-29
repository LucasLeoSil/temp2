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
        
def extractmax(arr):
    n = len(arr)
    arr[0], arr[-1] = arr[-1], arr[0]
    valor = arr.pop()
    heapify(arr, n, 0)
    print(valor)
    print(arr)

arr = [6,5,3,4,2,1]
extractmax(arr)