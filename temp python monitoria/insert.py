'''Lista 2,10,15,20'''
import random
def reverseheapify(heap, i):
    if i!=0:
        p = (i-1)//2
        if heap[p] < heap[i]:
            heap[p], heap[i] = heap[i], heap[p]
            reverseheapify(heap, p)


def insertheap(heap, valor):
    heap.append(valor)
    n = len(heap)-1
    reverseheapify(heap, n)
    print(heap)

heap = []
insertheap(heap, 2)
insertheap(heap, 10)
insertheap(heap, 15)
insertheap(heap, 20)
