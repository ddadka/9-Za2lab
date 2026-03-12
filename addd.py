import random
def sort_sel(spisok):
    arr = spisok.copy()
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    return arr, comparisons, swaps
import random
def sort_sel(spisok):
    arr=spisok.copy()
    n=len(arr)
    comparisons=0
    swaps=0
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            comparisons+=1
            if arr[j]<arr[min_index]:
                min_index=j
        if min_index!=i:
            arr[i],arr[min_index]=arr[min_index],arr[i]
            swaps+=1
    return arr,comparisons,swaps
def sort_bub(spisok):
    arr=spisok.copy()
    n=len(arr)
    comparisons=0
    swaps=0
    for i in range(n-1):
        swapped=False
        for j in range(n-1-i):
            comparisons+=1
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swaps+=1
                swapped=True
        if not swapped:
            break
    return arr,comparisons,swaps
def sort_quick(spisok):
    if len(spisok)<=1:
        return spisok,0,0
    pivot=spisok[len(spisok)//2]
    less=[]
    equal=[]
    greater=[]
    comparisons=0
    swaps=0
    for x in spisok:
        comparisons+=1
        if x<pivot:
            less.append(x)
            swaps+=1
        elif x>pivot:
            greater.append(x)
            swaps+=1
        else:
            equal.append(x)
    sorted_less,comp_less,swap_less=sort_quick(less)
    sorted_greater,comp_greater,swap_greater=sort_quick(greater)
    total_comparisons=comparisons+comp_less+comp_greater
    total_swaps=swaps+swap_less+swap_greater
    return sorted_less+equal+sorted_greater,total_comparisons,total_swaps
def 



