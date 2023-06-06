def binary_search(arr, target):
    
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == target:
            return True
        
        elif arr[middle] > target:
            right = middle -1

        else:
            left = middle + 1

    return False

def main():
    # True
    arr = [1, 3, 5, 7, 9]
    target = 5
    print(binary_search(arr, target))

    # False
    arr = [2, 4, 6, 8, 10]
    target = 7
    print(binary_search(arr, target))

    # False
    arr = []
    target = 5
    print(binary_search(arr, target))



if __name__ == "__main__":
    main()