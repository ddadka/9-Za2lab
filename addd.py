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


def print_table(results):
    print("\nМетод                | Сравнения      | Перестановки")
    print("-"*55)

    for name,comp,swp in results:
        print(name.ljust(20),"|",str(comp).ljust(14),"|",str(swp).ljust(14))


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

    print("\nОтсортированный массив:")
    print(sorted_sel)

    print_table(results)


def interactive_mode():
    size=int(input("Введите размер массива: "))
    arr=[random.randint(0,99) for _ in range(size)]

    while True:
        print("\nТекущий массив:")
        print(arr)

        print("\n1-Сортировка выбором")
        print("2-Сортировка пузырьком")
        print("3-Быстрая сортировка")
        print("4-Новый случайный массив")
        print("5-Ввести новый массив вручную")
        print("6-Изменить элемент по индексу")
        print("7-Добавить элемент")
        print("8-Удалить элемент")
        print("0-Выход")

        choice=input("Выберите действие: ")

        if choice=="1":
            sorted_arr,comp,swp=sort_sel(arr)
            print("Результат:",sorted_arr)
            print_table([("Выбором",comp,swp)])

        elif choice=="2":
            sorted_arr,comp,swp=sort_bub(arr)
            print("Результат:",sorted_arr)
            print_table([("Пузырьком",comp,swp)])

        elif choice=="3":
            sorted_arr,comp,swp=sort_quick(arr)
            print("Результат:",sorted_arr)
            print_table([("Быстрая",comp,swp)])

        elif choice=="4":
            arr=[random.randint(0,99) for _ in range(len(arr))]

        elif choice=="5":
            arr=list(map(int,input("Введите элементы через пробел: ").split()))

        elif choice=="6":
            index=int(input("Введите индекс элемента: "))
            if 0<=index<len(arr):
                value=int(input("Введите новое значение: "))
                arr[index]=value
            else:
                print("Неверный индекс!")

        elif choice=="7":
            value=int(input("Введите значение для добавления: "))
            arr.append(value)

        elif choice=="8":
            index=int(input("Введите индекс для удаления: "))
            if 0<=index<len(arr):
                arr.pop(index)
            else:
                print("Неверный индекс!")

        elif choice=="0":
            break

        else:
            print("Неверный ввод!")


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

            

    

