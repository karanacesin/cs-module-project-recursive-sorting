# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    arr =[] 
  
    while len(arrA) > 0 and len(arrB) > 0: 
        if arrA[0] < arrB[0]: 
            arr.append(arrA[0]) 
            arrA.pop(0) 
        else: 
            arr.append(arrB[0]) 
            arrB.pop(0) 

    for i in arrA: 
        arr.append(i) 
    for i in arrB: 
        arr.append(i) 


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):

    if len(arr) > 1: 
        mid = len(arr)//2
        l = merge_sort(arr[:mid]) 
        r = merge_sort(arr[mid:]) 

        #merge l and r
    
    merge_sort(merge(l,r))
  
        
                  
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here

