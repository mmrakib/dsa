def remove_duplicates(array):
    if not array:
        return None
    
    left = 0

    for right in range(1, len(array)):
        if array[left] != array[right]:
            left += 1
            array[left] = array[right]

    return left + 1

if __name__ == '__main__':
    array = [1, 1, 2, 2, 3, 4, 4, 5]
    length = remove_duplicates(array)

    print(array)
    print(length)