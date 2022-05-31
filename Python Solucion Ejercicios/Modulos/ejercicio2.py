
import time

hour = time.strftime('%H')
minutes = time.strftime('%M')

if int(hour) >= 19:
    print("Sales del trabajo")
else:
    print("Quedan {} horas y {} minutos para terminar tu jornada laboral",format(18- int(hour), 59-int(minutes)))