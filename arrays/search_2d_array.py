


def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    print("array search", arr, item)
    while(low<= high):
        mid = (low+high)//2
        print("search", low, high, mid, arr[mid])

        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            low = mid+1
        else:
            high = mid-1
    return -1

def better_solution(matrix, item):
    row_num = col_num = 0
    for i, row in enumerate(matrix):
        col = binary_search(row, item)
        if col != -1:
            row_num = i
            col_num = col
    return row_num, col_num

def better_solution_2(matrix, item):
    row = 0
    col = len(matrix[0]) - 1

    while row<len(matrix) and col>=0:
        if matrix[row][col] == item:
            return row, col

        if matrix[row][col] < item:
            row += 1
        elif matrix[row][col] > item:
            col -= 1
    else:
        return -1, -1

def optimal_solution(matrix, item):
    """ We try to flatten the 2d array to 1d array and run binary search
        Row num = 1d index/cols
        Col num = 1d index%cols
    """
    row = len(matrix)
    col = len(matrix[0]) - 1

    low, high = 0, (row*col) - 1

    while low <= high:
        mid = (low+high) // 2
        row_num = mid//col
        col_num = mid%col

        if matrix[row_num][col_num] == target:
            return row_num, col_num
        if matrix[row_num][col_num] < target:
            low = mid + 1
        else:
            high = mid - 1
    else:
        return -1, -1

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 23

print(better_solution(matrix, target))
print(better_solution_2(matrix, target))
print(optimal_solution(matrix, target))
