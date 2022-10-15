import datetime
import time

hora_actual = time.strftime('%H:%M:%S')
hora_salida = "19:00:00"

hora_actual = datetime.datetime.strptime(hora_actual, "%H:%M:%S")
hora_salida = datetime.datetime.strptime(str(hora_salida), "%H:%M:%S")


if hora_actual >= hora_salida:
    print('Hora de salir')

else:
    print ('Falta :', hora_salida - hora_actual)
