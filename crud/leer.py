import main
import sqlite3
import os
from tabulate import tabulate

class Leer:
    martillo = ''


# DATOS DE LOS MARTILLOS Y RESPECTIVAS CAMARAS
def consulta_uno():
    bd = sqlite3.connect('sub-6.db')
    cursor = bd.cursor()

    martillo = input('\nIngrese el martillo a consultar\n>>>')
    if not martillo:
        print('\nNo escribio nada\n')
        menu()

    # DATOS DE LA CONSULTA DE MARTILLO
    sentencia_martillo = "SELECT * FROM martillo WHERE ubicacion_martillo = ?"

    try:

        cursor.execute(sentencia_martillo, [martillo])

    except sqlite3.OperationalError as error:
        print('Error al abrir:', error)

    else:

        print('\nInformacion del Martillo.\n')

        print(tabulate(cursor,
                       headers=['Martillo', 'Numero Martillo', 'Firmware', 'IP Martillo', 'Power', 'CPU'],
                       tablefmt='grid'))

    # DATOS DE LA CONSULTA DE CAMARA 1
    sentencia_camara1 = "SELECT u_mart1, ip_camara1, modelo_cam1,usuario1, pass1 FROM camara1 WHERE u_mart1 = ?"

    try:
        cursor.execute(sentencia_camara1, [martillo])

    except sqlite3.OperationalError as error:
        print('Error al abrir:', error)

    else:
        print('\nInformacion de la Camara 1.\n')

        print(
            tabulate(cursor, headers=['Pertenece a', 'Ip Camara', 'Modelo de Camara', 'Usuario', 'Password', ],
                     tablefmt='grid'))

    # DATOS DE LA CONSULTA DE CAMARA 2
    sentencia_camara2 = "SELECT u_mart2, ip_camara2, modelo_cam2,usuario2, pass2 FROM camara2 WHERE u_mart2 = ?"

    try:
        cursor.execute(sentencia_camara2, [martillo])

    except sqlite3.OperationalError as error:
        print('Error al abrir:', error)

    else:
        print('\nInformacion de la Camara 2.\n')

        print(
            tabulate(cursor, headers=['Pertenece a', 'Ip Camara', 'Modelo de Camara', 'Usuario', 'Password', ],
                     tablefmt='grid'))

        print('')
        bd.close()
        menu()



# CONSULTA DE TODOS LOS MARTILLOS
def consulta_martillos():
    bd = sqlite3.connect('sub-6.db')
    cursor = bd.cursor()

    sentencia_martillo = "SELECT * FROM martillo"

    try:
        cursor.execute(sentencia_martillo)

    except sqlite3.OperationalError as error:
        print('Error al abrir:', error)

    else:
        print('\nInformacion de los Martillos.\n')

        print(tabulate(cursor,
                       headers=['Martillo', 'Numero Martillo', 'Firmware', 'IP Martillo', 'Power', 'CPU'],
                       tablefmt='grid'))

        print('')
        bd.close()
        menu()

    # CONSULTA DE TODAS LAS CAMARAS 1


def consulta_camara1():
    bd = sqlite3.connect('sub-6.db')
    cursor = bd.cursor()

    sentencia_camara1 = "SELECT u_mart1, ip_camara1, modelo_cam1,usuario1, pass1 FROM camara1"

    try:
        cursor.execute(sentencia_camara1)

    except sqlite3.OperationalError as error:
        print('Error al abrir:', error)

    else:
        print('\nInformacion de las Camaras 1.\n')

        print(tabulate(cursor, headers=['Pertenece a', 'Ip Camara', 'Modelo de Camara', 'Usuario', 'Password'],
                       tablefmt='grid'))

        print('')
        bd.close()
        menu()

    # CONSULTA DE TODAS LAS CAMARAS 2


def consulta_camara2():
    bd = sqlite3.connect('sub-6.db')
    cursor = bd.cursor()

    sentencia_camara2 = "SELECT u_mart2, ip_camara2, modelo_cam2,usuario2, pass2 FROM camara2"

    try:
        cursor.execute(sentencia_camara2)

    except sqlite3.OperationalError as error:
        print('Error al abrir:', error)

    else:
        print('\nInformacion de las Camaras 2.\n')

        print(tabulate(cursor, headers=['Pertenece a', 'Ip Camara', 'Modelo de Camara', 'Usuario', 'Password'],
                       tablefmt='grid'))

        print('')
        bd.close()
        menu()



def menu():
    # QUE CONSULTA DESEA REALIZAR
    print('\nElija la consulta que desea hacer\n')
    print('1 - Consulta individual del Martillo y sus Camaras')
    print('2 - Consulta todos los Martillos')
    print('3 - Consulta todas las Camaras 1')
    print('4 - Consulta todas las Camaras 2')
    print('9 - Salir')

    # SE LE SOLICITA UNA OPCION AL USUARIO
    opcion = input('\nIngrese la opcion deseada:\n>>>')
    if not opcion:
        print('\nNo escribio nada\n')
        menu()

    if opcion == '1':
        consulta_uno()
    elif opcion == '2':
        consulta_martillos()
    elif opcion == '3':
        consulta_camara1()
    elif opcion == '4':
        consulta_camara2()
    elif opcion == '9':
        print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        print('Gracias por utilizar la aplicacion.')
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
        os.system('clear')
        main.menu()

    else:
        print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        print('No se encuentra la opcion requerida, elija de nuevo!!!')
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
        menu()