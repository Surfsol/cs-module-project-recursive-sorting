# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    if len(arrA) == 0:
        return(sorted(arrB))
    if len(arrB) == 0:
        return(sorted(arrA))

    arrA.sort()
    A = arrA
    print(A)
    arrB.sort()
    B = arrB
    print(B)

    #merged_arr = [0 for _ in range(len(arrA) + len(arrB))]
    merged = []
    pA = 0
    pB = 0

    while len(merged) < (len(arrA)+len(arrB)):
        #print(merged, 'pA', pA, A[pA],  'pB', pB)
        
        
        if pA <= len(A) and pB > len(B)-1:
            merged.append(A[pA])
            pA += 1
        elif pB <= len(B) and pA > len(A)-1:
            merged.append(B[pB])
            pB += 1
        elif  A[pA] <= B[pB]:
            print('merge A',A[pA] )
            merged.append(A[pA])
            pA += 1
        elif A[pA] > B[pB]:
            print('merge B',B[pB] )
            merged.append(B[pB])
            pB += 1

    return merged 

    
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [2]
arr4 = [0, 1, 2, 3, 4, 5]

print(merge(arr1, arr4))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # if len(arr) == 0:
    #     return 
    #split array and make recursive
    if len(arr) > 1:
        half = len(arr) // 2

        low = merge_sort(arr[0:len(arr) // 2])
        high = merge_sort(arr[len(arr) // 2:])
        arr = merge(low, high)
    return arr
    #base return array of 1 value
    
    

# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(merge_sort(arr1))
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

