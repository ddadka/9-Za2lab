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
def demo_mode():
    size=20
    arr=[random.randint(0,99) for _ in range(size)]
    print("Исходный массив:")
    print(arr)
    results=[]
    sorted_sel,comp_sel,swap_sel=sort_sel(arr)
    sorted_bub,comp_bub,swap_bub=sort_bub(arr)
    sorted_quick_arr,comp_quick,swap_quick=sort_quick(arr)
    results.append(("Выбором",comp_sel,swap_sel))
    results.append(("Пузырьком",comp_bub,swap_bub))
    results.append(("Быстрая",comp_quick,swap_quick))
    print("Отсортированный массив:")
    print(sorted_sel)
    for i in results:
        print(i[0],'сравнения,перестановки:',i[1],i[2])
def interactive_mode():
    size=20
    arr=[random.randint(0,99) for _ in range(size)]  
    while True:      
        print("Текущий массив:")
        print(arr)
        print("1-Сортировка выбором")
        print("2-Сортировка пузырьком")
        print("3-Быстрая сортировка")
        print("4-Ввести новый массив вручную")
        print("5-Изменить элемент по индексу")
        print("0-Выход")
        choice=input("Выберите действие: ")
        if choice=="1":
            sorted_arr,comp,swp=sort_sel(arr)
            print('')
            print('массив:',sorted_arr,'сравнения,перестановки:',comp,swp)
            print('')
        elif choice=="2":
            sorted_arr,comp,swp=sort_bub(arr)
            print('')
            print(sorted_arr,'сравнения,перестановки:',comp,swp)
            print('')
        elif choice=="3":
            sorted_arr,comp,swp=sort_quick(arr)
            print('')
            print(sorted_arr,'сравнения,перестановки:',comp,swp)
            print('')
        elif choice=="4":
            arr=list(map(int,input('Введите массив:').split()))
        elif choice=="5":
            elem=input('Введите элемент:')
            ind=input('Введите индекс:')
            elem=int(elem)
            ind=int(ind)
            arr[ind]=elem
def main():
    print("1-Демонстрационный режим")
    print("2-Интерактивный режим")
    mode=input("Выберите режим: ")
    if mode=="1":
        demo_mode()
    elif mode=="2":
        interactive_mode()
    else:
        print("Неверный выбор!")
if __name__=="__main__":
    main()

            

    


