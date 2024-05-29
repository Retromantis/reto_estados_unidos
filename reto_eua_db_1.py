
#-------------------------------------------------------------------
#
#                            EJERCICIO 1
#
#-------------------------------------------------------------------

import mysql.connector as myconector;

conect= myconector.connect(user='root', password ='', host = 'localhost', database = 'estados_unidos', port = "3306")
query = conect.cursor()

query.execute("""CREATE TABLE Estados (
                    Id_Estado INTEGER PRIMARY KEY NOT NULL,
                    Nombre VARCHAR(30) NOT NULL,
                    Fecha_Fundacion VARCHAR(8) NOT NULL,
                    Latitud VARCHAR(20) NOT NULL,
                    Longitud VARCHAR(20) NOT NULL
                );
             """)


query.execute("""CREATE TABLE Poblacion (
                    Id_Poblacion INTEGER PRIMARY KEY,
                    Id_Estado INTEGER NOT NULL,
                    Anio INTEGER NOT NULL,
                    Cantidad INTEGER NOT NULL
                    );
             """)

query.execute("""CREATE TABLE Muertes (
                    Id_Muertes INTEGER PRIMARY KEY,
                    Id_Estado INTEGER NOT NULL,
                    Anio INTEGER NOT NULL,
                    Cantidad INTEGER NOT NULL
                );
             """)


query.execute("""CREATE TABLE Residentes_65 (
                    Id_Residente INTEGER PRIMARY KEY,
                    Id_Estado INTEGER NOT NULL,
                    Anio INTEGER NOT NULL,
                    Cantidad INTEGER NOT NULL
                );
             """)


