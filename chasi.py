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
print('введите часы и минуты:')
vrem = list(map(str, input().split()))
hours=vrem[0]
minutes=vrem[1]
dlin_vvod=len(vrem)
def prov(hours, minutes):
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
    if 0 <= hours <= 5:
        return 'ночи'
    if 6 <= hours <= 11:
        return 'утра'
    if 12 <= hours <= 17:
        return 'дня'
    if 18 <= hours <= 23:
        return 'вечера'
if dlin_vvod!=2:
    print('Введены неверные данные: значения должны быть введины как XX XX')    
elif hours[0]=='-' or minutes[0]=='-':
    print('Введены неверные данные:все значения должны быть положительными')
elif prov(int(hours),int(minutes)) == '1':
    if str(hours) + str(minutes) == '00':
        print('полночь')
    elif str(hours) + str(minutes) == '120':
        print('полдень')
    elif prov_min(int(minutes)) != ' ровно':
        print(str(int(hours)) + prov_chas(int(hours)) + str(int(minutes)) + prov_min(int(minutes)) + vrem_sut(int(hours)))
    else:
        print(str(int(hours)) + prov_chas(int(hours)) + vrem_sut(int(hours)) + prov_min(int(minutes)))
