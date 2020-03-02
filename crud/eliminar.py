import sqlite3
import main
import os
import getpass


class Eliminando:
    eliminar = ''


def eliminar_todo():
    bd = sqlite3.connect('sub-6.db')
    cursor = bd.cursor()

    eliminar = input('\nIngrese el Martillo a Eliminar\n>>>')

    # SENTENCIA PARA ELIMINAR CAMARA 1
    sentencia_cam1 = "DELETE FROM camara1 WHERE u_mart1 = ?"

    try:
        cursor.execute(sentencia_cam1, [eliminar])

    except sqlite3.OperationalError as error:
        print('Error al abrir:', error)

    else:
        bd.commit()
        print('\nEliminado el dato de la Tabla camara 1 con Exito')

    # SENTENCIA PARA ELIMINAR CAMARA 2
    sentencia_cam2 = "DELETE FROM camara2 WHERE u_mart2 = ?"

    try:
        cursor.execute(sentencia_cam2, [eliminar])

    except sqlite3.OperationalError as error:
        print('Error al abrir:', error)

    else:
        bd.commit()
        print('Eliminado el dato de la Tabla camara 2 con Exito')

    # SENTENCIA PARA ELIMINAR MARRTILLO
    sentencia = "DELETE FROM martillo WHERE ubicacion_martillo = ?"

    try:
        cursor.execute(sentencia, [eliminar])

    except sqlite3.OperationalError as error:
        print('Error al abrir:', error)

    else:
        bd.commit()
        bd.close()
        os.system('clear')
        print('Eliminado el dato de la Tabla Martillo con Exito\n')
        menu()


def menu():
    print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print('Elija la opcion a seguir')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
    print('1 - Eliminando Datos')
    print('9 - Salir, volver a menu principal')

    opcion = input('\nIngrese una opcion:\n>>>')
    if not opcion:
        print('\nNo escribio nada\n')
        print('Vuelva a intentarlo\n')
        menu()

    if opcion == '1':
        os.system('clear')
        eliminar_todo()
    elif opcion == '9':
        os.system('clear')
        main.menu()


def validar_pass(password):
    return password == 'grupo1'


def principal():
    print('\n\tDebe estar registrado para ingresar, introdusca su contraseña:\n')

    password = getpass.getpass()

    if validar_pass(password):
        print('\n\tContraseña Correcta')
        print('\n\tBienvenido a Eliminar Datos')
        menu()

    else:
        print('\n\tContraseña Incorrecta')
        main.menu()
