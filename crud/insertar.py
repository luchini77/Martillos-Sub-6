import os
import sqlite3
import main
import getpass


class Insertar:
    u_martillo = ''
    num_martillo = ''
    firmware = ''
    ip_martillo = ''
    power_plc = ''
    cpu = ''
    ip_camara1 = ''
    modelo_cam1 = ''
    usuario_cam1 = ''
    pass_cam1 = ''
    u_mart1 = ''
    ip_camara2 = ''
    modelo_cam2 = ''
    usuario_cam2 = ''
    pass_cam2 = ''
    u_mart2 = ''


# PUNTAPIE INICIAL A INSERTAR
def iniciar_martillo():
    insertar_datos_martillo()
    insertar_datos_camara1()
    insertar_datos_camara2()


# DATOS DEL MARTILLO
def insertar_datos_martillo():
    bd = sqlite3.connect('sub-6.db')
    cursor = bd.cursor()

    os.system('clear')
    print('\nIngrese los datos del Martillo.')
    u_martillo = input('\nMartillo:\n>>>')
    num_martillo = input('Numero de Martillo:\n>>>Martillo ')
    firmware = input('Firmware:\n>>>')
    ip_martillo = input('Ip Martillo:\n>>>')
    power_plc = input('Modelo de Power:\n>>>')
    cpu = input('CPU:\n>>>')

    # INSERTANDO DATOS A LA TABLA MARTILLO

    sentencia_martillo = "INSERT INTO martillo(ubicacion_martillo, numero_martillo, firmware, ip_martillo,power_plc, " \
                         "cpu) VALUES (?,?,?,?,?,?) "

    try:
        cursor.execute(sentencia_martillo, [u_martillo, num_martillo, firmware, ip_martillo, power_plc, cpu])

    except sqlite3.OperationalError as error:
        print('Error al abrir:', error)

    else:
        bd.commit()
        bd.close()
        print('\nGuardado Correctamente Datos del Martillo')


# DATOS DE LA CAMARA 1
def insertar_datos_camara1():
    bd = sqlite3.connect('sub-6.db')
    cursor = bd.cursor()

    print('\nIngrese datos de la Camara 1.')
    ip_camara1 = input('\nIP camara 1:\n>>>')
    modelo_cam1 = input('Modelo de Camara:\n>>>')
    usuario_cam1 = input('Nombre Usuario:\n>>>')
    pass_cam1 = input('Password:\n>>>')
    u_mart1 = input('A que martillo pertenece la camara:\n>>>')

    # INSERTANDO DATOS A LA TABLA CAMARA 1

    sentencia_camara1 = "INSERT INTO camara1(ip_camara1, modelo_cam1, usuario1, pass1, u_mart1) VALUES (?,?,?,?,?)"

    try:
        cursor.execute(sentencia_camara1, [ip_camara1, modelo_cam1, usuario_cam1, pass_cam1, u_mart1])

    except sqlite3.OperationalError as error:
        print('Error al abrir:', error)

    else:
        bd.commit()
        bd.close()
        print('\nGuardado Correctamente Datos de la Camara 1')


# DATOS DE LA CAMARA 2
def insertar_datos_camara2():
    bd = sqlite3.connect('sub-6.db')
    cursor = bd.cursor()

    print('\nIngrese datos de la Camara 2.')
    ip_camara2 = input('\nIP camara 2:\n>>>')
    modelo_cam2 = input('Modelo de Camara:\n>>>')
    usuario_cam2 = input('Nombre Usuario:\n>>>')
    pass_cam2 = input('Password:\n>>>')
    u_mart2 = input('A que martillo pertenece la camara:\n>>>')

    # INSERTANDO DATOS A LA TABLA CAMARA 2

    sentencia_camara2 = "INSERT INTO camara2(ip_camara2, modelo_cam2, usuario2, pass2, u_mart2) VALUES (?,?,?,?,?)"

    try:
        cursor.execute(sentencia_camara2, [ip_camara2, modelo_cam2, usuario_cam2, pass_cam2, u_mart2])

    except sqlite3.OperationalError as error:
        print('Error al abrir:', error)

    else:
        bd.commit()
        bd.close()
        print('\nGuardado Correctamente Datos de la Camara 2')

        seguir()


def seguir():
    print('\n\t===============')
    print('\tQue desea hacer')
    print('\t===============\n')
    print('1 - Insertar datos de Martillo y Camaras')
    print('9 - Volver a Menu Principal')

    opcion = input('\nIngrese una opcion:\n>>>')
    if not opcion:
        print('\nNo escribio nada\n')
        print('Vuelva a intentarlo\n')
        seguir()

    if opcion == '1':
        os.system('clear')
        iniciar_martillo()

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
        print('\n\tBienvenido a Insertar Datos')
        seguir()

    else:
        print('\n\tContraseña Incorrecta')
        main.menu()
