import sys
from random import random
from datetime import datetime


# Ejercicio 1.a: Solución desarrollada por María Tapia

# crea una lista que contenga un diccionario por cada estado. Cada elemento de la lista será un diccionario
estados = ["Alabama", "Florida", "Georgia", "South Carolina"]
poblacion_2000 = [4447100, 15982378, 8186453, 4012012]
poblacion_2001 = [4451493, 17054000, 8229823, 4023438]
residentes_2000 = [3870598, 13237167, 7440877, 3535770]
residentes_2001 = [3880476, 13548077, 7582146, 3567172]
muertes_2000 = [10622, 38103, 14804, 8581]
muertes_2001 = [15912, 166069, 15000, 9500]
latitudes = [33.258882, 27.756767, 32.329381, 33.687439]
longitudes = [-86.829534, -81.463983, -83.113737, -80.436374]
fechas_fundacion = ["14-12-1819", "03-03-1845", "12-02-1733", "26-03-1776"]

datos_estados = []

for estado, pop_2000, pop_2001, res_2000, res_2001, muertes_2000, muertes_2001, lat, lon, fecha in zip(
    estados, poblacion_2000, poblacion_2001, residentes_2000, residentes_2001, muertes_2000, muertes_2001, latitudes, longitudes, fechas_fundacion
):
    datos_estados.append({
        "estado": estado,
        "poblacion_2000": pop_2000,
        "poblacion_2001": pop_2001,
        "resid_menor_65_2000": res_2000,
        "resid_menor_65_2001": res_2001,
        "muertes_2000": muertes_2000,
        "muertes_2001": muertes_2001,
        "latitud": lat,
        "longitud": lon,
        "fecha_fundacion": fecha
    })


# busca en la lista un estado por nombre y lo devuelve por Victor Zegarra
def buscar_estado(nombre):
    diccionario = {}
    nombre = nombre.lower()
    for estado in datos_estados:
        if estado['estado'].lower() == nombre:
            diccionario = estado
            break
    return diccionario


# Ejercicio 1.b: Solución desarrollada por Victor Zegarra

# busca en la lista un estado y devuelve un nuevo diccionario
def genenar_diccionario_estado(nombre):
    diccionario = {}
    estado = buscar_estado(nombre)
    if estado:
        for key in estado.keys():
            diccionario[key + '_' + nombre] = estado[key]
    return diccionario


# Ejercicio 1.c: Solución desarrollada por María Tapia

# correción de la población del estado de Florida
def corregir_poblacion_florida():
    # Agregar un nuevo valor al diccionario
    estado = buscar_estado('Florida')
    if estado:                 
        estado['poblacion_2001'] = 16054328    # se ingresa a la clave Población 2001 y colocamos el nuevo valor 


# Ejercicio 1.d: Solución desarrollada por Victor Zegarra y Rafael

# calcular los días desde su fundación de los estados    
def calcular_dias_desde_fundacion():
    for estado in datos_estados:
        date_str = estado['fecha_fundacion']
        format_str = "%d-%m-%Y"                             # cadena con formato "dd-mm-aaaa"
        fundacion = datetime.strptime(date_str, format_str) # convertir fecha con formato "dd-mm-aaaa" a objeto datetime
        dias = datetime.today() - fundacion                              # calcular el delta (diferencía de días)
        estado['dias_desde_fundacion'] = dias.days          # guadar los días transcurridos en un nuevo campo 


# Ejercicio 1.e: Solución desarrollada por Rafael

# calcular el porcentaje de personas mayores de 65 años en cada estado 
def porcentaje_mayores_65():
    #Realizamos para los mayores de 65 años en el 2000
    for estado in datos_estados:
        res_menor = estado['resid_menor_65_2000']
        total_pob = estado['poblacion_2000']

        porcentaje_mayor = ((total_pob - res_menor)/total_pob)*100
        porcentaje_mayor = round(porcentaje_mayor, 2)
        
        estado['porcentaje_mayor_65_años_2000'] = porcentaje_mayor


    #Luego, realizamos para los mayores de 65 años en el 2001

    for estado in datos_estados:
        res_menor = estado['resid_menor_65_2001']
        total_pob = estado['poblacion_2001']

        porcentaje_mayor = ((total_pob - res_menor)/total_pob)*100
        porcentaje_mayor = round(porcentaje_mayor, 2)
        
        estado['porcentaje_mayor_65_años_2001'] = porcentaje_mayor


# Ejercicio 1.f: Solución desarrollada por Victor Zegarra

# mostrar el estado más antiguo y el más moderno, y la difencia de años entre ellos
def estado_antiguo_moderno():
    mas_dias = 0
    menos_dias = sys.maxsize

    for estado in datos_estados:
        dias = estado['dias_desde_fundacion']
        if dias > mas_dias:     # buscar el estado con más días desde su fundación
            mas_dias = dias
            mas_antiguo = estado
        if dias < menos_dias:   # buscar el estado con ménos días desde su fundación
            menos_dias = dias
            mas_moderno = estado

    años_antiguo = mas_dias // 365      
    años_moderno = menos_dias // 365      
    años_diferencia = años_antiguo - años_moderno    

    print('El estado más antiguo es',mas_antiguo['estado'],'con',años_antiguo,'años desde su fundación')
    print('El estado más moderno es',mas_moderno['estado'],'con',años_moderno,'años desde su fundación')
    print('La diferencia en años entre el estado más antiguo y el más moderno es de',años_diferencia,'años')

def listar_estados():
    # Imprimir la lista de diccionarios
    for estado in datos_estados:
        print(estado)   


# Ejercicio 2: **** INCOMPLETO ****

def calcular_crecimiento_poblacion():
    alabama = genenar_diccionario_estado('Alabama')
    south_carolina = genenar_diccionario_estado('South Carolina')
    ratio_1 = random()
    ratio_2 = random()
    alabama['ratio_crecimiento'] = min(ratio_1,ratio_2)
    south_carolina['ratio_crecimiento'] = max(ratio_1,ratio_2)

    print(alabama)
    print(south_carolina)
    # TODO 


# Ejercicio 3: Solución desarrollada por María Tapia

#Creamos la funcion:
def proyeccion_poblacion_demografia(año_1, año_2):

    #Hacemos una nueva lista e iteramos solo los datos que necesitaremos: estados, poblacion 2000, 2001 y fecha fundacion:
    info_estados = []

    for estado, pobl_1, pobl_2, fund  in zip(estados, poblacion_2000, poblacion_2001, fechas_fundacion):
        info_estados.append({
            'estado': estado,
            'poblacion_2000': pobl_1,
            'poblacion_2001': pobl_2,
            'fecha_fundacion': fund
        })

    for estado in info_estados:
        pobl_1 = estado['poblacion_' + str(año_1)]    #Obtenemos las claves donde el año_1 ingresado es convertido en string para que pueda agregarse al texto y ser ubicado
        pobl_2 = estado['poblacion_' + str(año_2)]    #Igual con el año_2
        
        # Proyección de la población para el año siguiente al año_2
        ratio = pobl_2 / pobl_1
        proximo_año = año_2 + 1
        poblacion_proyectada = ratio * pobl_2
        
        # Calculamos t desde la fundación hasta 1900
        ''' Obtenemos el año de fundacion haciendo un .split que separara la fecha por cada "-" 
        que encontremos (ejemplo: "14-12-1819" lo pasa a: "14" "12" "1819") y con el [-1] selecciona 
        al ultimo elemento, en este caso el año'''  
        año_fundacion = int(estado['fecha_fundacion'].split("-")[-1])   
        t = 1900 - año_fundacion
        
        # Función demográfica P(t)
        P_t = (14500 * t + 7000) / (2 * t + 1)
        
        # Añadimos resultados al diccionario del estado
        estado['poblacion_' + str(proximo_año)] = poblacion_proyectada
        estado['poblacion_demografica'] = P_t

    for estado in info_estados:
        print(estado)


# Ejercicio 3: Solución desarrollada por Patricio

#Instrucciones reto 1.3
#Cread una función que genere una proyección para el año 2002, utilizando como ratio
#la comparativa entre los años 2000 y 2001. De tal forma:
#Población Año 2002 = Población Año 2001 / Población Año 2000 x Población año 2001.
#Tras un estudio demográfico se ha determinado que el número de habitantes de cierta población, 
#en los próximos años, vendrá dado por la función: P(t) = 14500t + 7000/2t + 1 donde t son los años transcurridos entre
#la fundación del Estado y 1900.
#En la misma función, devolved la población que tendría cada Estado bajo la estimación que devuelve ese estudio demográfico.
#Añadid los resultados a cada diccionario de la lista.


# que hacer ? 
# 1) creo la funcion que genera proyeccion para el 2002

def func_ecu_pobla2002(poblacion_2000, poblacion_2001):
    return (poblacion_2001 / poblacion_2000) * poblacion_2001


# 2) creo la funcion para calcular poblacion usando ecuacion demografica P(t) = 14500t + 7000/2t + 1 (como tomamos la ecuacion ?)

def func_ecu_demografica(t):
    # AQUI HAY QUE DISCUTIR DE QUE MANERA LA TOMAMOS, los parentesis
    return (14500 * t) + (7000/(2*t) + 1)


# 2.2) (hacer t= año de fundacion - 1900), funcion p(t), resultado P(t) para cada estado


def func_edit_proyecydemo():
    for estado in datos_estados:
        # Proyección para el año 2002
        estado['poblacion_2002'] = func_ecu_pobla2002(estado['poblacion_2000'], estado['poblacion_2001'])
        
        # Calculo años desde la fundación hasta 1900
        fecha_fundacion = datetime.strptime(estado['fecha_fundacion'], "%d-%m-%Y")
        
        # AQUI HAY QUE REVISAR SI LA RESTA NO ES  AL REVÉS, MENCIONA LA DIFERENCIA PERO ESTO DEPENDE DE LA FECHA DE FUNDACION SI ES ANTERIOR O POSTERIOR
        t = 1900 - fecha_fundacion.year
        # (entendi de que debe ser para cada estado)
        
        # Población demográfica
        estado['poblacion_demografica'] = func_ecu_demografica(t)



calcular_dias_desde_fundacion()
corregir_poblacion_florida()
porcentaje_mayores_65()
estado_antiguo_moderno()
print()
#print(genenar_diccionario_estado('alabama'))
#calcular_crecimiento_ploblacion()

#llamado del ejercicio 3: Solucionado por María
proyeccion_poblacion_demografia(2000, 2001)
print()

#llamado del ejercicio 3: Soluciónado por Patricio
func_edit_proyecydemo()

# 3) Muestra diccionarios y resultados finales
listar_estados()