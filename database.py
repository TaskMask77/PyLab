import mysql.connector
#Import a specific error for to work
from mysql.connector import Error

# Usaremos la Sentencia  (_try Except_) para intertar connectar la base de Datos
# Caso contrario o de no poder conectarse Mostrara un error Especifico
try:
    conexion = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='1234567',
        db='uni'
    )
    if(conexion.is_connected()):
        print("Succesfully connection...!")
        #Ask to the system about MariaDatabase Version, if do you wanna see, have to delete '#'

        #info_bae = conexion.get_server_info()
        #info_2 = conexion.get_server_version()
        #print(f"Info Server :{info_bae}  \nVersion:{info_2}")

        # the  object called 'Cursor' help us to find and browse above the db table
        cursor = conexion.cursor()
        cursor.execute("SELECT database();")
        registro = cursor.fetchone()
        print(f"You connected to Database called :{registro}")
        
        # Usamos el obj Cursor para recorrer las Tablas de nuestra base de Datos que hemos creado
        # E imrimiremos el resultado usando FORloops y la palabra reservada Fetchall(mostrar todo)
        #Finalmente imprimimos el  numero de registros realizados con la sentencia (cursor.rowcount)
        cursor.execute("SELECt *FROM student")
        resultados = cursor.fetchall()
        for i in resultados:
            print(i[0] , i[1] , i[2] , i[3])
        print(f"Register counted : {cursor.rowcount}")

#Caso de no conectar mostara un mesaje de error y el tipo de Error        
except Error as ex:
    print(f"We couldn't connect to the database | Type error :{ex}")

# Finalmente ejecutara el 'finally' y cerrara cesion con mysql
finally:
    #Finalizamos la coneccion preguntando primeramente si la base de datos esta coonectada
    if conexion.is_connected():
        conexion.close()
        print("Finished session...!")