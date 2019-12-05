# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


# insertion sort

def insertion_sort(arr):
    # loop through n-1 elements
    for i in range(1, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # i = index - 1

# checking our cur_index which is i is greater than 0, and checking that the left element is greater than the right element.
        while cur_index > 0 and arr[cur_index-1] > arr[cur_index]:
            cur_index[i] = cur_index[i-1]
        # TO-DO: swap
            cur_index[i-1] = smallest_index
            cur_index -= 1

    return arr
