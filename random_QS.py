from numpy import random
import time

def partitionHoare(arr, low, high):
    pivot_index = random.randint(low, high + 1)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    
    pivot = arr[high]
    i = low - 1
    j = high
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quickSortHoare(arr, low, high):
    if low < high:
        pi = partitionHoare(arr, low, high)
        quickSortHoare(arr, low, pi)
        quickSortHoare(arr, pi + 1, high)

def partitionLomuto(arr, low, high):
    pivot_index = random.randint(low, high + 1)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSortLomuto(arr, low, high):
    if low < high:
        pi = partitionLomuto(arr, low, high)
        quickSortLomuto(arr, low, pi - 1)
        quickSortLomuto(arr, pi + 1, high)

arrH = random.randint(10000000, size=(100000))
arrL = arrH.copy()
n = len(arrH)

start = time.time()
quickSortHoare(arrH, 0, n - 1)
end = time.time()

start1 = time.time()
quickSortLomuto(arrL, 0, n - 1)
end1 = time.time()

print(f'Time Hoare: {end - start}')
print(f'Time Lomuto: {end1 - start1}')
