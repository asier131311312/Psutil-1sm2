import psutil
print("INFORMACIÓN DEL SISTEMA")
print("**********************")
print("Tiempon de los procesos")
info = psutil.cpu_times()
print("Tiempo de procesos del usuario: "+str(info.user))
print("Tiempo de procesos del sistema: "+str(info.system))

print(psutil.cpu_times())


