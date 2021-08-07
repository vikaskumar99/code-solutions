"""
Inversion Count for an array indicates – how far (or close) the array is from being sorted. If the array is already sorted, then the inversion count is 0, but if the array is sorted in the reverse order, the inversion count is the maximum.
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

Input: arr[] = {8, 4, 2, 1}
Output: 6

Explanation: Given array has six inversions:
(8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).


Input: arr[] = {3, 1, 2}
Output: 2

Explanation: Given array has two inversions:
(3, 1), (3, 2)

"""


def brute_force(arr):
    inv_count = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1

    return inv_count


def better_solution(arr):
    temp = [0] * len(arr)
    inv_count = merge_sort(arr, temp, 0, len(arr) - 1)
    return inv_count


def merge_sort(arr, temp, left, right):
    inv_count = 0

    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort(arr, temp, left, mid)
        inv_count += merge_sort(arr, temp, mid + 1, right)

        inv_count += merge(arr, temp, left, mid, right)
    return inv_count


def merge(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            temp[k] = arr[j]
            j += 1
            k += 1
            inv_count += mid - i + 1
    while(i<=mid):
        temp[k] = arr[i]
        k+=1
        i+=1
    while(j<=right):
        temp[k] = arr[j]
        k+=1
        j+=1

    for loop_var in range(left, right + 1):
        arr[loop_var] = temp[loop_var]
    return inv_count


arr = [3,1,2]
print(brute_force(arr))
print(better_solution(arr))