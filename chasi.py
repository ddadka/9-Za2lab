hours, minutes = map(int, input().split())


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


if prov(hours, minutes) == '1':
    if str(hours) + str(minutes) == '00':
        print('полночь')
    elif str(hours) + str(minutes) == '120':
        print('полдень')
    elif prov_min(int(minutes)) != ' ровно':
        print(str(hours) + prov_chas(int(hours)) + str(minutes) + prov_min(int(minutes)) + vrem_sut(hours))
    else:
        print(str(hours) + prov_chas(int(hours)) + vrem_sut(hours) + prov_min(int(minutes)))
