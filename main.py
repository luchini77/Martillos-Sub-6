from crud import borrar
from crud import eliminar
from crud import insertar
from crud import modificar
from crud import leer
import os


def menu():
    os.system('clear')

    while True:
        print('\n\t************************************************')
        print('\tBienvenido a la aplicacion Claves del Sub-6')
        print('\t************************************************\n')
        print('1 - Consultar Datos')
        print('2 - Insertar Datos')
        print('3 - Actulizar Datos')
        print('4 - Eliminar Datos')
        print('9 - Salir')

        opc = input('\nIntrocuce una opcion: \n>>>')
        if not opc:
            print('\nNo escribio nada\n')
            print('Vuelva a intentarlo\n')
            menu()

        if opc == '1':
            os.system('clear')
            leer.menu()

        elif opc == '2':
            os.system('clear')
            insertar.principal()

        elif opc == '3':
            os.system('clear')
            modificar.principal()

        elif opc == '4':
            os.system('clear')
            eliminar.principal()

        elif opc == '9':

            os.system('clear')
            print('\n\t===================================')
            print('\tGracias por utilizar la aplicacion.')
            print('\t===================================\n')
            exit()


menu()
