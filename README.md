import psutil
import pandas as pd

print("INFORMACIÓN DEL SISTEMA")
print("**********************")
print("Tiempon de los procesos")
info = psutil.cpu_times()
print("Tiempo de procesos del usuario: "+str(info.user))
print("Tiempo de procesos del sistema: "+str(info.system))



data = {'Lunes':[1],
        'Martes':[2],
        'Miercoles':[3],
        'Jueves':[4],
        'Viernes':[3],
        'Sabado':[4],
        'Domingo':[3]}

df = pd.DataFrame(data, columns = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'])

print(df)

df = pd.to_excel('example.xlsx')

print(psutil.cpu_times())
feiffiefj
