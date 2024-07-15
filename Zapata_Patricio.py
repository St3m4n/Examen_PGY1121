#https://github.com/St3m4n/Examen_PGY1121
from os import system
from random import randint
from statistics import geometric_mean, mean

system("cls")

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
                 "Laura Hermández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
sueldos = []
trabajadores_con_sueldo = []

def asignar_sueldos():
    sueldos = []
    for _ in range(10):
        sueldos.append(randint(300000, 2500000))
    contador = 0
    trabajadores_con_sueldo = []
    for trabajador in trabajadores:
        trabajadores_con_sueldo.append([trabajador, sueldos[contador]])
        contador +=1
    print("Sueldos asignados...")
    return trabajadores_con_sueldo, sueldos

def clasificar_sueldos():
    if len(trabajadores_con_sueldo) > 0:
        menor_a_ocho = []
        entre_ocho_y_dosm = []
        mas_de_dosm = []
        total = 0
        for trabajador in trabajadores_con_sueldo:
            if trabajador[1] < 800000:
                menor_a_ocho.append(trabajador)
            elif trabajador[1] > 800000 and trabajador[1] < 2000000:
                entre_ocho_y_dosm.append(trabajador)
            else:
                mas_de_dosm.append(trabajador)
            total = total + trabajador[1]
        if len(menor_a_ocho) > 0:
            print(f'''
                Sueldos Menores a $800.000.- TOTAL:{len(menor_a_ocho)}''')
            print('''
                    Nombre empleado            Sueldo''')
            for trabajador in menor_a_ocho:
                print(f'''
                    {trabajador[0]}                 ${trabajador[1]}
                ''')
        if len(entre_ocho_y_dosm) > 0:
            print(f'''
                Sueldos entre $800.000.- y $2.000.000.- TOTAL:{len(entre_ocho_y_dosm)}
                ''')
            print('''
                    Nombre empleado            Sueldo''')
            for trabajador in entre_ocho_y_dosm:
                print(f'''
                    {trabajador[0]}            ${trabajador[1]}
                ''')
        if len(mas_de_dosm) > 0:
            print(f'''
                Sueldos superiores a $2.000.000.- TOTAL:{len(mas_de_dosm)}''')
            print('''
                    Nombre empleado            Sueldo''')
        for trabajador in mas_de_dosm:
                print(f'''
                    {trabajador[0]}            ${trabajador[1]}
                ''')
        print(f'''Total sueldos:      {total}''')
    else:
        print("No se registran sueldos para asignar...")
    return

def ver_estadisticas():
    if len(trabajadores_con_sueldo) > 0:
        sueldo_mas_alto = max(sueldos)
        sueldo_mas_bajo = min(sueldos)
        promedio_sueldos = mean(sueldos)
        media_geometrica = geometric_mean(sueldos)
        print(f'''
        * Sueldo más alto:          {sueldo_mas_alto}
        * Sueldo más bajo:          {sueldo_mas_bajo}
        * Promedio de sueldos:      {promedio_sueldos}
        * Media geométrica:         {media_geometrica:.2f}
        ''')
    else:
        print("No se registran sueldos para generar estadisticas...")
    return

def reporte_sueldos():    
    if len(trabajadores_con_sueldo) >0:
        reporte = []
        print('''
            Nombre empleado     Sueldo Base     Descuento Salud     Descuento AFP       Sueldo Líquido
        ''')
        for trabajador in trabajadores_con_sueldo:
            salud = int(trabajador[1]*0.07)
            afp = int(trabajador[1]*0.12)
            liquido = int(trabajador[1] - salud - afp)
            reporte.append([trabajador[0], trabajador[1], salud, afp, liquido])
            print(f'''
            {trabajador[0]}         {trabajador[1]}         {salud}         {afp}       {liquido}
            ''')
        archivo = open("reporte_sueldos.csv", "w")
        archivo.write("Nombre empleado;Sueldo Base;Descuento Salud;Descuento AFP;Sueldo Líquido\n")
        for datos in reporte:
            archivo.write(";".join(map(str, datos))+"\n")
        archivo.close()
        print("Se a generado un archivo .csv para su revisión...")      
    else:
        print("No se registran sueldos para generar datos...")
    return

while True:
    print('''
    1.-Asignar sueldos aleatorios
    2.-Clasificar sueldos
    3.-Ver estadísticas
    4.-Reporte de sueldos
    5.-Salir del programa
    ''')
    op = input("Ingrese la funcion que desea ejecutar...")
    match op:
        case "1":
            system("cls")
            trabajadores_con_sueldo, sueldos = asignar_sueldos()
        case "2":
            system("cls")
            clasificar_sueldos()
        case "3":
            system("cls")
            ver_estadisticas()
        case "4":
            system("cls")
            reporte_sueldos()
        case "5":
            system("cls")
            print("Finalizando programa...")
            print("Desarrollado por Patricio Zapata")
            print("RUT 18.525.428-3")
            break
        case other:
            print("Opción ingresada no valida...")