def quick_sort(arr : list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    arr1 = [item for item in arr[1:] if item <= pivot]
    arr2 = [item for item in arr[1:] if item > pivot]
    
    return quick_sort(arr1) + [pivot] + quick_sort(arr2)
           
