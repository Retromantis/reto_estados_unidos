#-------------------------------------------------------------------
#
#                            EJERCICIO 3
#
#-------------------------------------------------------------------

#-------------------------------------------------------------------
#
#                     Consultar tablas de MySQL
#
#-------------------------------------------------------------------

import mysql.connector as myconector;
import pymongo

conect= myconector.connect(user='root', password ='', host = 'localhost', database = 'estados_unidos', port = "3306")
cursor = conect.cursor()

def convertir_tabla_a_coleccion(tabla, keys):
    coleccion = []
    cursor.execute("SELECT * FROM " + tabla)
    list = cursor.fetchall()
    for values in list:
        dictionary = dict(zip(keys, values))
        coleccion.append(dictionary)
    return coleccion    

coleccion_estados = convertir_tabla_a_coleccion('estados', ('Id_Estado', 'Nombre', 'Fecha_Fundacion', 'Latitud', 'Longitud'))
print('\nEstados:\n', coleccion_estados)

coleccion_poblacion = convertir_tabla_a_coleccion('poblacion', ('Id_Poblacion', 'Id_estado', 'Anio', 'cantidad'))
print('\nPoblación:\n', coleccion_poblacion)

coleccion_muertes = convertir_tabla_a_coleccion('muertes', ('Id_Muertes', 'Id_estado', 'Anio', 'cantidad'))
print('\nMuertes:\n', coleccion_muertes)

coleccion_residentes = convertir_tabla_a_coleccion('residentes_65', ('Id_Residentes', 'Id_estado', 'Anio', 'cantidad'))
print('\nResidentes < 65:\n', coleccion_residentes)

cursor.close()


#-------------------------------------------------------------------
#
#       Insertar datos en MongoDB desde las tablas de MySQL
#
#-------------------------------------------------------------------

MONGO_HOST = "localhost"
MONGO_PORT = "27017"
MONGO_TIME_OUT = 1000
MONGO_URL = "mongodb://"+MONGO_HOST+":"+MONGO_PORT+"/" 

def insertar_coleccion(collection_name, collection_data):
    collection = db[collection_name]
    collection.insert_many(collection_data)

def mostrar_documentos(collection_name):
    print(f'\n{collection_name}:\n')
    collection = db[collection_name]
    list = collection.find({})
    for document in list:
        print(document)

try:
    client = pymongo.MongoClient(MONGO_URL,serverSelectionTimeoutMS=MONGO_TIME_OUT)
    client.server_info()
    print("\nConexión con mongo exitosa")

    db = client["estados_unidos"]

    insertar_coleccion('estados', coleccion_estados)
    insertar_coleccion('muertes', coleccion_muertes)
    insertar_coleccion('poblacion', coleccion_poblacion)
    insertar_coleccion('residentes_65', coleccion_residentes)

    mostrar_documentos('estados')
    mostrar_documentos('muertes')
    mostrar_documentos('poblacion')
    mostrar_documentos('residentes_65')

    client.close()

except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido de carga", errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb", errorConexion)