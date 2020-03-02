import main
import sqlite3
import os
import getpass


class Actualizar:
    martillo = ''


def menu_martillo():
    bd = sqlite3.connect('sub-6.db')
    cursor = bd.cursor()

    print('\nQue dato desea modificar del martillo?\n')
    print('1 - Ubicacion del Martillo')
    print('2 - Numero del Martillo')
    print('3 - Firmware')
    print('4 - Ip del Martillo')
    print('5 - Power del PLC')
    print('6 - CPU')
    print('9 - Salir Menu Principal')

    opcion = input('\nInserta una opcion\n>>> ')
    if not opcion:
        print('\nNo escribio nada\n')
        print('\nVuelva a elegir una opcion\n!!!')
        menu_martillo()

    if opcion == '1':

        ubicacion_martillo = input('\nIngrese el martillo a Modificar\n>>>')

        u_mart = input('\nIngrese nueva ubicacion del Martillo:\n>>>')

        sentencia_martillo = "UPDATE martillo SET ubicacion_martillo=? WHERE ubicacion_martillo=?"

        try:
            cursor.execute(sentencia_martillo, [u_mart, ubicacion_martillo])

        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)

        else:
            bd.commit()
            bd.close()
            os.system('clear')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            print('Dato actualizado exitosamente.')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            menu()

    elif opcion == '2':

        ubicacion_martillo = input('\nIngrese el martillo a Modificar\n>>>')

        num_mart = input('\nIngrese el nuevo Numero del Martillo:\n>>>')

        sentencia_martillo = "UPDATE martillo SET numero_martillo=? WHERE ubicacion_martillo=?"

        try:
            cursor.execute(sentencia_martillo, [num_mart, ubicacion_martillo])

        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)

        else:
            bd.commit()
            bd.close()
            os.system('clear')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            print('Dato actualizado exitosamente.')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            menu()

    elif opcion == '3':

        ubicacion_martillo = input('\nIngrese el martillo a Modificar\n>>>')

        firm = input('\nIngrese el nuevo Firmware:\n>>>')

        sentencia_martillo = "UPDATE martillo SET firmware=? WHERE ubicacion_martillo=?"

        try:
            cursor.execute(sentencia_martillo, [firm, ubicacion_martillo])

        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)

        else:
            bd.commit()
            bd.close()
            os.system('clear')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            print('Dato actualizado exitosamente.')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            menu()

    elif opcion == '4':

        ubicacion_martillo = input('\nIngrese el martillo a Modificar\n>>>')

        ip_mart = input('\nIngrese la nueva Ip del Martillo:\n>>>')

        sentencia_martillo = "UPDATE martillo SET ip_martillo=? WHERE ubicacion_martillo=?"

        try:
            cursor.execute(sentencia_martillo, [ip_mart, ubicacion_martillo])

        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)

        else:
            bd.commit()
            bd.close()
            os.system('clear')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            print('Dato actualizado exitosamente.')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            menu()

    elif opcion == '5':

        ubicacion_martillo = input('\nIngrese el martillo a Modificar\n>>>')

        power_plc = input('\nIngrese la Nueva Power del PLC:\n>>>')

        sentencia_martillo = "UPDATE martillo SET power_plc=? WHERE ubicacion_martillo=?"

        try:
            cursor.execute(sentencia_martillo, [power_plc, ubicacion_martillo])

        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)

        else:
            bd.commit()
            bd.close()
            os.system('clear')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            print('Dato actualizado exitosamente.')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            menu()

    elif opcion == '6':

        ubicacion_martillo = input('\nIngrese el martillo a Modificar\n>>>')

        cpu = input('\nIngrese la Nueva CPU del PLC:\n>>>')

        sentencia_martillo = "UPDATE martillo SET cpu=? WHERE ubicacion_martillo=?"

        try:
            cursor.execute(sentencia_martillo, [cpu, ubicacion_martillo])

        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)

        else:
            bd.commit()
            bd.close()
            os.system('clear')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            print('Dato actualizado exitosamente.')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            menu_martillo()

    elif opcion == '9':
        os.system('clear')
        main.menu()


def menu_camara1():
    bd = sqlite3.connect('sub-6.db')
    cursor = bd.cursor()

    print('\nQue dato desea modificar de la Camara 1?\n')
    print('1 - Ip de la Camara')
    print('2 - Modelo de Camara')
    print('3 - Usuario')
    print('4 - Password')
    print('5 - A que martillo pertenece la Camara')
    print('9 - Salir Menu Principal')

    opcion = input('\nInserta una opcion\n>>> ')
    if not opcion:
        print('\nNo escribio nada\n')
        menu_camara1()

    if opcion == '1':

        ubicacion_martillo = input('\nIngrese el martillo a Modificar\n>>>')

        ip_cam1 = input('\nIngrese nueva Ip de la Camara 1:\n>>>')

        sentencia_camara1 = "UPDATE camara1 SET ip_camara1=? WHERE u_mart1=?"

        try:
            cursor.execute(sentencia_camara1, [ip_cam1, ubicacion_martillo])

        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)

        else:
            bd.commit()
            bd.close()
            os.system('clear')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            print('Dato actualizado exitosamente.')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            menu()

    elif opcion == '2':

        ubicacion_martillo = input('\nIngrese el martillo a Modificar\n>>>')

        modelo_cam1 = input('\nIngrese el modelo de la Camara 1:\n>>>')

        sentencia_camara1 = "UPDATE camara1 SET modelo_cam1=? WHERE u_mart1=?"

        try:
            cursor.execute(sentencia_camara1, [modelo_cam1, ubicacion_martillo])

        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)

        else:
            bd.commit()
            bd.close()
            os.system('clear')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            print('Dato actualizado exitosamente.')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            menu()

    elif opcion == '3':

        ubicacion_martillo = input('\nIngrese el martillo a Modificar\n>>>')

        usuario_cam1 = input('\nIngrese el usuario de la Camara 1:\n>>>')

        sentencia_camara1 = "UPDATE camara1 SET usuario1=? WHERE u_mart1=?"

        try:
            cursor.execute(sentencia_camara1, [usuario_cam1, ubicacion_martillo])

        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)

        else:
            bd.commit()
            bd.close()
            os.system('clear')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            print('Dato actualizado exitosamente.')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            menu()

    elif opcion == '4':

        ubicacion_martillo = input('\nIngrese el martillo a Modificar\n>>>')

        pass_cam1 = input('\nIngrese password de la Camara 1 del:\n>>>')

        sentencia_camara1 = "UPDATE camara1 SET pass1=? WHERE u_mart1=?"

        try:
            cursor.execute(sentencia_camara1, [pass_cam1, ubicacion_martillo])

        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)

        else:
            bd.commit()
            bd.close()
            os.system('clear')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            print('Dato actualizado exitosamente.')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            menu()

    elif opcion == '5':

        ubicacion_martillo = input('\nIngrese el martillo a Modificar\n>>>')

        u_mart1 = input('\nIngrese a que martillo pertenece la Camara 1:\n>>>')

        sentencia_camara1 = "UPDATE camara1 SET u_mart1=? WHERE u_mart1=?"

        try:
            cursor.execute(sentencia_camara1, [u_mart1, ubicacion_martillo])

        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)

        else:
            bd.commit()
            bd.close()
            os.system('clear')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            print('Dato actualizado exitosamente.')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            menu_camara1()

    elif opcion == '9':
        os.system('clear')
        main.menu()


def menu_camara2():
    bd = sqlite3.connect('sub-6.db')
    cursor = bd.cursor()

    print('\nQue dato desea modificar de la Camara 2?\n')
    print('1 - Ip de la Camara')
    print('2 - Modelo de Camara')
    print('3 - Usuario')
    print('4 - Password')
    print('5 - A que martillo pertenece la Camara')
    print('9 - Salir')

    opcion = input('\nInserta una opcion\n>>> ')
    if not opcion:
        print('\nNo escribio nada\n')
        menu_camara2()

    if opcion == '1':

        ubicacion_martillo = input('\nIngrese el martillo a Modificar\n>>>')

        ip_cam2 = input('\nIngrese nueva Ip de la Camara 2:\n>>>')

        sentencia_camara2 = "UPDATE camara2 SET ip_camara2=? WHERE u_mart2=?"

        try:
            cursor.execute(sentencia_camara2, [ip_cam2, ubicacion_martillo])

        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)

        else:
            bd.commit()
            bd.close()
            os.system('clear')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            print('Dato actualizado exitosamente.')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            menu()

    elif opcion == '2':

        ubicacion_martillo = input('\nIngrese el martillo a Modificar\n>>>')

        modelo_cam2 = input('\nIngrese el modelo de la Camara 2:\n>>>')

        sentencia_camara2 = "UPDATE camara2 SET modelo_cam2=? WHERE u_mart2=?"

        try:
            cursor.execute(sentencia_camara2, [modelo_cam2, ubicacion_martillo])

        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)

        else:
            bd.commit()
            bd.close()
            os.system('clear')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            print('Dato actualizado exitosamente.')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            menu()

    elif opcion == '3':

        ubicacion_martillo = input('\nIngrese el martillo a Modificar\n>>>')

        usuario_cam2 = input('\nIngrese el usuario de la Camara 2:\n>>>')

        sentencia_camara2 = "UPDATE camara2 SET usuario2=? WHERE u_mart2=?"

        try:
            cursor.execute(sentencia_camara2, [usuario_cam2, ubicacion_martillo])

        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)

        else:
            bd.commit()
            bd.close()
            os.system('clear')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            print('Dato actualizado exitosamente.')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            menu()

    elif opcion == '4':

        ubicacion_martillo = input('\nIngrese el martillo a Modificar\n>>>')

        pass_cam2 = input('\nIngrese password de la Camara 2:\n>>>')

        sentencia_camara2 = "UPDATE camara2 SET pass2=? WHERE u_mart2=?"

        try:
            cursor.execute(sentencia_camara2, [pass_cam2, ubicacion_martillo])

        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)

        else:
            bd.commit()
            bd.close()
            os.system('clear')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            print('Dato actualizado exitosamente.')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            menu()

    elif opcion == '5':

        ubicacion_martillo = input('\nIngrese el martillo a Modificar\n>>>')

        u_mart2 = input('\nIngrese a que martillo pertenece la Camara 2:\n>>>')

        sentencia_camara2 = "UPDATE camara2 SET u_mart2=? WHERE u_mart2=?"

        try:
            cursor.execute(sentencia_camara2, [u_mart2, ubicacion_martillo])

        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)

        else:
            bd.commit()
            bd.close()
            os.system('clear')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            print('Dato actualizado exitosamente.')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
            menu_camara2()

    elif opcion == '9':
        os.system('clear')
        main.menu()


def menu():
    print('\nElija que item desea actualizar\n')
    print('1 - Modificar datos en Martillos')
    print('2 - Modificar datos de la Camara 1')
    print('3 - Modificar datos de la Camara 2')
    print('9 - Salir a menu Principal')

    # SE LE SOLICITA UNA OPCION AL USUARIO
    opcion = input('\nIngrese la opcion deseada:\n>>>')
    if not opcion:
        print('\nNo escribio nada\n')
        print('\nVUelve a intentar\n')
        menu()

    if opcion == '1':
        os.system('clear')
        menu_martillo()

    elif opcion == '2':
        os.system('clear')
        menu_camara1()

    elif opcion == '3':
        os.system('clear')
        menu_camara2()

    elif opcion == '9':
        os.system('clear')
        main.menu()
    else:
        print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        print('No se encuentra la opcion requerida, elija de nuevo!!!')
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
        menu()


def validar_pass(password):
    return password == 'grupo1'


def principal():
    print('\n\tDebe estar registrado para ingresar, introdusca su contraseña:\n')

    password = getpass.getpass()

    if validar_pass(password):
        print('\n\tContraseña Correcta')
        print('\n\tBienvenido a Actualizar Datos')
        menu()

    else:
        print('\n\tContraseña Incorrecta')
        main.menu()

