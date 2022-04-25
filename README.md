import psutil
import csv
from csv import DictWriter

import pandas as pd
import openpyxl
import os
from datetime import date
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

import seaborn as sns
import matplotlib.pyplot as plt
csv = pd.read_csv(r'tiempos.csv', sep=",")
res =sns.scatterplot(x="fecha", y="sistema",data=csv)
plt.show()


print(psutil.cpu_times())
