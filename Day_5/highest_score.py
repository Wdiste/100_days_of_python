# This is an example of a search and a sort

# Find the highest number

scores = [76, 87, 78, 108, 59, 78, 75, 99, 76, 55]
top_score = 0
for score in scores:
    if score > top_score:
        top_score = score

print(top_score)

# this is a insertion sort

def insertion_sort(arr):
    # key is current index. j is the index before the key.
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

    # while j doesnt exceed the first index
    # if the value at the current index is less than the value before it,
    # shift that value one index to the right and check the next (decreasing) index

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

    # when the key is no longer less than the value at the previous index,
    # the current index is given the value of the key

        arr[j + 1] = key

    return arr

array = [32, 54, 24, 76, 45, 29, 954, 23, 57, 42, 61, 37, 678, 312, 57, 2]
print("Unsorted array: ", array)
sorted_array = insertion_sort(array)
print("Sorted array: ", sorted_array)