#Crear directorios ya establecidos sobre Fechas - Actividades Luren

import os
from os.path import join
from datetime import date
#m = 2000
#simyear = today.year - m

def CrearDirectorios(day):
    monthsname=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    months={"Jan":"Enero","Feb":"Febrero","Mar":"Marzo","Apr":"Abril",
    "May":"Mayo","Jun":"Junio","Jul":"Julio","Aug":"Agosto","Sep":"Septiembre",
    "Oct":"Octubre","Nov":"Noviembre","Dec":"Diciembre"}
    monthswithdays={"Enero":31,"Febrero":28,"Marzo":31,"Abril":30,
    "Mayo":31,"Junio":30,"Julio":31,"Agosto":31,"Septiembre":30,
    "Octubre":31,"Noviembre":30,"Diciembre":31}
    if today.year%4==0:
        monthswithdays["Febrero"]=29
    countdays={"Mon":0,"Tue":1,"Wed":2,"Thu":3,"Fri":4,"Sat":5,"Sun":6}
    monthActualStr=months[today.ctime().split(' ')[1]]
    path=r"C:\Users\diego\Desktop\Actividades_SL"
    onlyfiles=[f for f in os.listdir(path)]
    lastFile=""
    Monday=today.day-countdays[day]
    Friday=Monday+4
    if Monday==0:
        mon=list(monthswithdays.values())[list(months.keys()).index(monthActualStr)-1]
        lastFile=f"Semana {mon} - {Friday}"
    elif Monday<0:
        mon=list(monthswithdays.values())[list(months.keys()).index(monthActualStr)-1]
        lastFile=f"Semana {today.day-countdays[day]+mon} - {Friday}"
    elif Friday>monthswithdays[monthActualStr]:
        lastFile=f"Semana {Monday} - {Friday-monthswithdays[monthActualStr]}"
    else:
        lastFile=f"Semana {Monday} - {Friday}"
    direxist=[]
    dircreates=[]
    print(f"Nombre de la carpeta {lastFile}")
    for i in onlyfiles:
        if os.path.isfile(join(path,i)):continue
        if i in ["(Otros)","Compartido"]:continue
        dirmonth=join(path,i,monthActualStr)
        dirtocreate=join(path,i,monthActualStr,lastFile)
        if os.path.exists(dirmonth):
            if os.path.exists(dirtocreate):
                direxist.append(dirtocreate)
                #print(f"\nLa siguiente ruta ya existe:\n-> {dirtocreate}")
            else:
                os.mkdir(dirtocreate)
                dircreates.append(dirtocreate)
                #print(f"\nLa siguiente ruta ha sido creada:\n-> {dirtocreate}\n")
        else:
            os.makedirs(dirtocreate)
            dircreates.append(dirtocreate)
            #print(f"\nLa siguiente ruta ha sido creada:\n-> {dirtocreate}\n")
    if len(direxist)>0:
        print(f"Existen ({len(direxist)}):")
        for r in direxist:
            print(f"    -> {r}")
    else:
        print("No existe ninguna ruta")
    print()
    if len(dircreates)>0:
        print(f"Rutas Creadas ({len(dircreates)}):")
        for c in dircreates:
            print(f"    -> {c}")
    else:
        print("No se ha creado ninguna carpeta")

#Ejecucion principal
print("Creando...")
print()
today=date.today()
dayActualStr=today.ctime().split(' ')[0]
CrearDirectorios(dayActualStr)
print()
sm = input("Presione enter para salir...")