import psutil
import csv
from csv import DictWriter
import numpy as np
import pandas as pd
import openpyxl
import os
from datetime import date
import matplotlib.pyplot as plt
import seaborn as sns
print("INFORMACIÓN DEL SISTEMA")
print("**********************")
print("Tiempo de los procesos")

hoy = date.today()


tiempos = psutil.cpu_times()
estadisticas = psutil.cpu_stats()
memoria = psutil.virtual_memory()
file_exists = os.path.isfile("tiempos.csv")
headersCSV = ['fecha','usuario','sistema','inactividad']      
dict={'fecha':hoy,'usuario':tiempos.user,'sistema':tiempos.system,'inactividad':tiempos.idle}

  
with open('tiempos.csv', 'a', newline='') as f_object:
    dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
    if not file_exists:
        dictwriter_object.writeheader()
    dictwriter_object.writerow(dict)
   
    f_object.close()


csv = pd.read_csv(r'tiempos.csv', sep=",")
puntosx = np.array(csv['fecha'])
puntosy= np.array(csv['sistema'])


plt.subplot (2, 3, 1)
plt.plot(puntosx,puntosy)
plt.title("Tiempo de uso")

puntosx = np.array(csv['fecha'])
puntosy= np.array(csv['usuario'])


plt.axhline(y=3500, color='r', linestyle='-')


plt.subplot (2, 3, 2)
plt.plot(puntosx,puntosy)
plt.title("Tiempo de usuario")

puntosx = np.array(csv['fecha'])
puntosy= np.array(csv['inactividad'])


plt.axhline(y=5000, color='r', linestyle='-')


plt.subplot (2, 3, 3)
plt.plot(puntosx,puntosy)
plt.title("Tiempo de inactividad")



plt.axhline(y=200000, color='r', linestyle='-')

plt.suptitle("Graficas PC ")
plt.show()
 
print(psutil.cpu_times())





