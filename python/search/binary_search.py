def binary_search(array, target):
    low = 0
    hi = len(array) - 1

    while low <= hi:
        mid = low + (hi - low) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            hi = mid - 1

    return None
