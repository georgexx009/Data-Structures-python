#Bubble Sort

def bubble_sort(arr):
    for el in arr:
        print(arr)
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp

nums = [5, 2, 9, 1, 5, 6]
print(nums)
bubble_sort(nums)
print("-----------")
print(nums)



def bubble_sort_opt(arr):
    for i in range(len(arr)):
        #iterate through unplaced elements
        for idx in range(len(arr) - 1 - i):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                

nums_2 = [5, 2, 9, 1, 5, 6]
print("-------------------")
print("-------------------")
bubble_sort_opt(nums_2)
print(nums_2)