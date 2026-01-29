import random
def sort_sel(spisok):
    for ind in range(len(spisok)-1):
        min_el=min(spisok[ind:])
        min_ind=(spisok[ind:].index(min_el))+ind
        spisok[ind],spisok[min_ind]=spisok[min_ind],spisok[ind]
    return  spisok,len(spisok),sum([i for i in range(len(spisok)])
def sort_bub(spisok):
    spisok_1=spisok.copy()
    spisok_1.sort()
    while spisok_1!=spisok:
        for ind_1 in range(len(spisok)-1):
            if spisok[ind_1+1]<spisok[ind_1]:
                spisok[ind_1+1],spisok[ind_1]=spisok[ind_1],spisok[ind_1+1]
                
    return spisok
def sort_del(spisok):
    bolshe=[]
    menshe=[]
    seredina=[]
    if len(spisok) <= 1:
        return spisok
    nach=spisok[len(spisok)//2]
    for elem in spisok:
        if elem>nach:
            bolshe.append(elem)
        elif elem<nach:
            menshe.append(elem)
        else:
            seredina.append(elem)
    return sort_del(menshe)+seredina+sort_del(bolshe)
print('напиши 1 для демонстрации программы')
print('напиши 2 для изменения массива')
vvod=int(input())
if vvod==1:
    


            
    