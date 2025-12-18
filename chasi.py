'''
алгоритм

пользователь вводит данные 
данные считываются
произвдится проверка верного ввода данны:
  если часы и минуты заданы положительными числами,часы от 00 до 23 и минуты от 00 59 и если длина ввода равна 4 
    то введённые данные верены  
  иначе
    введённые данные не верны
еcли данные верны то произвродится проверка на особы случаи:
  если введённые пользвователем данные это 00 00:
    то вывести полночь
  если введённые пользвователем данные это 12 00:
    то вывести полдень
если введённые данные не являются особым случаем:
то проверка на склонение минут:
  если минуты равны 00 то это особый случай и будет 'ровно'
  если колво минут заканчивается на 1 и минуты не от 10 до 19 то склонение 'минута'
  если минуты от 10 до 19 или заканчиваются на 0,5,6,7,8,9 то склоннение 'минут'
  если минуты заканчиваются на 2,3,4 то склонение 'минуты'
после проверки на минуты проверка на часы:
  если колво часов заканчивается на 1 и не от 10 до 19 то склонение 'час'
  если минуты от 10 до 19 или заканчиваются на 0,5,6,7,8,9 то склоннение 'часов'
  если минуты заканчиваются на 2,3,4 то склонение 'часа'
проверка на время суток:
  если часы от 0 до 6(не включительно) то время суток 'ночь'
  если часы от 6 до 12(не включительно) то время суток 'утро'
  если часы от 12 до 18(не включительно) то время суток 'день'
  если часы от 18 до 24(не включительно) то время суток 'вечер'
если проверка на то минуты равны 00:
 если это так то ввывести ответ для этого случая
если нет:
 то вывести ответ
'''
def prov(hours, minutes):
    if (hours < 0 or hours > 23) and (minutes < 0 or minutes > 59):
        return print('Введены недопустимые данные: часы и минуты должны быть в пределах значений')
    elif hours < 0 or hours > 23:
        return print('Введены недопустимые данные: часы должны быть от 0 до 23.')
    elif minutes < 0 or minutes > 59:
        return print('Введены недопустимые данные: минуты должны быть от 0 до 59.')
    else:
        return True


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
    if 18 <= hours < 24:
        return 'вечера'
def main():
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
        if prov(hours_znach,minutes_znach) == True:
            if hours_znach  == 0 and minutes_znach == 0:
                print('полночь')
            elif hours_znach  == 12 and minutes_znach == 0:
                print('полдень')
            elif prov_min(minutes_znach)!= ' ровно':
                print(hours + prov_chas(hours_znach) + minutes + prov_min(minutes_znach) + vrem_sut(hours_znach))
            else:
                print(hours + prov_chas(hours_znach) + vrem_sut(hours_znach) + prov_min(minutes_znach))
if __name__ == "__main__":
    main()


