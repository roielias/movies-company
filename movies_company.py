# first inefficient algorithm that count the invertions betwween members in the array
def count_invertions_A(arr):
    counter = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                counter += 1
    return counter


# second inefficient algorithm that count the invertions betwween members in the array and Also count the size of the inversion
def count_invertions_B(arr):
    counter = 0
    size_sum = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                counter += 1
                size_sum += arr[i] - arr[j]
    return counter, size_sum


# this is a simple merge sort function for understand our count invertions function
def merge(left,right):
    merged = []
    i = j = 0
    while i > len(left) and j > len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    start = arr[:mid]
    end = arr[mid:]
    sorted_start = merge_sort(start)
    sorted_end = merge_sort(end)
    return merge(sorted_start,sorted_end)


# third efficient algorithm that count the invertions betwween members in the array:
def count_invertions_C(arr):
    if len(arr) <= 1:
        return arr,0
    
    mid = len(arr) // 2
    left_sorted, left_inversions = count_invertions_C(arr[:mid])
    right_sorted, right_inversions = count_invertions_C(arr[mid:])

    merged = []
    i = j = 0
    inversions = 0

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            j += 1
            inversions += len(left_sorted) - i
    merged.extend(left_sorted[i:])
    merged.extend(right_sorted[j:])

    total_inversions = left_inversions + right_inversions + inversions
    return merged, total_inversions    


# fourth efficient algorithm that count the invertions betwween members in the array and also check the the size of inversions:
def count_inversions_D(arr):
    if len(arr) <= 1:
        return arr, 0, 0
    
    mid = len(arr) // 2
    left_sorted, left_inversions, left_size = count_inversions_D(arr[:mid])
    right_sorted, right_inversions, right_size = count_inversions_D(arr[mid:])

    merged = []
    i = j = 0
    inversions = 0
    inversion_size = 0

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            inversions += len(left_sorted) - i
            inversion_size += sum(left_sorted[i:]) - (len(left_sorted) - i) * right_sorted[j]
            j += 1

    merged.extend(left_sorted[i:])
    merged.extend(right_sorted[j:])

    total_inversions = left_inversions + right_inversions + inversions
    total_size = left_size + right_size + inversion_size

    return merged, total_inversions, total_size
print(count_inversions_D([1,3,4,2]))
