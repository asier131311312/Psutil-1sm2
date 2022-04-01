import psutil
import pandas as pd
import openpyxl
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
        'Viernes':[5],
        'Sabado':[6],
        'Domingo':[7]}

df = pd.DataFrame(data, columns = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'])

print(df)
wb = openpyxl.example.xlsx
hoja = wb.active
df = pd.to_excel('example.xlsx')

print(psutil.cpu_times())
