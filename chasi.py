'''
алгоритм

вывод приветственного сообщения с просьбой ввести время
ввод времени


функция на проверку правильного ввода часов и минут:
 1.проверка на то что и часы и минуты введены неправильно
 2.проверка на то что часы введены не правильно
 3.проверка на то что минуты введены не правлиьно
 
 
функция на проверку минут:
 1.минуты равны нулю
 2.количество минут заканчивается на 1
 3.количество минут заканчивается на цифры от 5 до 9 и 0 или минуты от 10 до 20
 4.количество минут заканчивается на цифры от 2 до 4
аналогичная фйнкция для проверки часов


функция на проверку времени суток:
 1.от 0 до 5 часов ночь
 2.от 6 до 11 часов утро
 3.от 12 до 17 часов день
 4.от 18 до 23 часов вечер
 
 
проверка на вверную длину ввода:
 вывод верной ошибки
проверка на положительность ввода:
 вывод верной ошибки
использование функции на проверку правильного вводы часов и минут:
 вывод верной ошибки 
проверка на полдень и полночь:
 вывод ответа в правильном формате 
проверка на то что кол-во минут равно 0:
 вывод ответа в правильном формате 
'''
if __name__ == "__main__":
    Main(def prov(hours, minutes):
    if (hours < 0 or hours > 23) and (minutes < 0 or minutes > 59):
        return print('Введены недопустимые данные: часы и минуты должны быть в пределах значений')
    elif hours < 0 or hours > 23:
        return print('Введены недопустимые данные: часы должны быть от 0 до 23.')
    elif minutes < 0 or minutes > 59:
        return print('Введены недопустимые данные: минуты должны быть от 0 до 59.')
    else:
        return '1'


def prov_min(minutes):
    last_digit = minutes % 10
    if minutes == 0:
        return ' ровно'
    if last_digit == 1 and minutes // 10 != 1:
        return ' минута '
    if last_digit >= 5 or last_digit < 1 or minutes // 10 == 1:
        return ' минут '
    if 1 < last_digit < 5:
        return ' минуты '


def prov_chas(hours):
    last_digit = hours % 10
    if last_digit == 1 and hours // 10 != 1:
        return ' час '
    if last_digit >= 5 or last_digit < 1 or hours // 10 == 1:
        return ' часов '
    if 1 < last_digit < 5:
        return ' часа '


def vrem_sut(hours):
    if 0 <= hours < 6:
        return 'ночи'
    if 6 <= hours < 12:
        return 'утра'
    if 12 <= hours < 18:
        return 'дня'
    if 18 <= hours < 18:
        return 'вечера'
print('введите часы и минуты:')
vrem = list(map(str, input().split()))
dlin_vvod=sum([len(i) for i in vrem])
if dlin_vvod!=4:
    print('Введены неверные данные: значения должны быть введины как XX XX')
elif not (vrem[0].isdigit() and vrem[1].isdigit()):
    print('Введены неверные данные:все значения должны быть положительными')
else:
    hours=vrem[0]
    minutes=vrem[1]
    hours_znach=int(hours)
    minutes_znach=int(minutes)    
    if prov(hours_znach,hours_znach) == '1':
        if hours + minutes == '0000':
            print('полночь')
        elif hours + minutes == '1200':
            print('полдень')
        elif prov_min(minutes_znach)!= ' ровно':
            print(hours + prov_chas(hours_znach) + minutes + prov_min(minutes_znach) + vrem_sut(hours_znach))
        else:
            print(hours + prov_chas(hours_znach) + vrem_sut(hours_znach) + prov_min(minutes_znach)))
