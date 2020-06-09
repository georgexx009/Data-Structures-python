#Quicksort
#Doing this "in place" is to not create a new variable, use the same one
from random import randrange
def quicksort(myList, start, end):
    if start >= end:
        return
    
    pivotIdx = randrange(start, end + 1)
    pivotValue = myList[pivotIdx]
    
    myList[end], myList[pivotIdx] = myList[pivotIdx], myList[end]
    
    mid_pointer = start
    
    for i in range(start, end):
        if myList[i] < pivotValue:
            myList[i], myList[mid_pointer] = myList[mid_pointer], myList[i]
            mid_pointer += 1
    
    myList[mid_pointer], myList[end] = myList[end], myList[mid_pointer]
    
    quicksort(myList, start, mid_pointer - 1)
    quicksort(myList, mid_pointer + 1, end)
    
my_list = [6, 8, 4, 14, 2, 19, 1, 10, 9, 17]
quicksort(my_list, 0, len(my_list) - 1)
print(my_list)
    
#[4,3,{8},6]
#[4,3,6,{8}]
#[(4),3,6,{8}]

#[{4},3,8,6]
#[3,8,6,7,5,{4}]
#[({3}),8,6,7,5,{{4}}]
#[3,{(8)},6,7,5,{{4}}]
#[3,{8},6,7,5,{{4}}]
#[3,{{4}},6,7,5,{8}]

#[3]

#[4,6,{{7}},5,8]
#[({4}),6,8,5,{{7}}]
#[(4),{6},8,5,{{7}}]
#[4,(6),{8},5,{{7}}]
#[4,6,({8}),5,{{7}}]
#[4,6,{8},(5),{{7}}] #[4,6,5,({8}),{{7}}]
#[4,6,{5},(8),{{7}}]  

#[8]