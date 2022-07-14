#!/usr/bin/env python3

######## ЗАДАНИЕ 2 ########
sectime = input('Введи время в секундах, а я скажу его в часах и минутах ')

hours = int(sectime) // 3600
minutes = (int(sectime) - hours * 3600) // 60
seconds = (int(sectime) - (hours * 3600) - (minutes * 60))

print('В',sectime,f'Секундах: Часов {hours:02} Минут {minutes:02} секунд {seconds:02}')