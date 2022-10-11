# ARCHIVO PRINCIPAL
# Autor: Ricardo Cárdenas Guevara
# Fecha de creación: 10/10/2022

from encryption_utils import *
from file_utils import *
from input_utils import *

encryption_key = generateKey()
want_exit = False

while not want_exit:
    print('\n==============================')
    print('SISTEMA DE CIFRADO DE MENSAJES')
    print('==============================')
    print('Llave de cifrado:\n[' + encryption_key + ']')
    
    print('\nOpciones:')
    print('1.- Cifrar mensaje')
    print('2.- Descifrar mensaje')
    print('3.- Generar llave de cifrado')
    print('4.- Importar llave de cifrado')
    print('5.- Exportar llave de cifrado')
    print('6.- Salir')
    
    option = select_option('\nSelecciona una opción:', range(1, 7))
    if option == 1:
        print('\nCIFRAR MENSAJE')
        print('\nOpciones:')
        print('1.- Escribir')
        print('2.- Leer desde archivo')
        print('3.- Cancelar')
        
        option = select_option('\nSelecciona una opción:', range(1, 4))
        if (option != 3):
            message = ''
            if option == 1:
                message = input('\nIngresa el mensaje:\n')
            elif option == 2:
                message = get_message(input('\nIngresa el nombre del archivo:\n'))
            if message:
                encrypted_message = encrypt(message, encryption_key)
            
                print('\nEl mensaje cifrado es:')
                print(encrypted_message)
                print('------------------------------')
                if confirm_option('\n¿Deseas guardar el resultado?'):
                    filename = input('\nIngresa el nombre del archivo a guardar\n')
                    if (save_message(filename, encrypted_message)):
                        print('\n-- Mensaje guardado en archivo ' + filename + '.txt --')
                        wait()
                    else:
                        print('\n[!] No se pudo guardar el archivo [!]')
                        wait()
            else:
                print('\n[!] No se pudo obtener el mensaje [!]')
                wait()
        else:
            print('\n-- Acción cancelada --')
            wait()
    elif option == 2:
        print('\nDESCIFRAR MENSAJE')
        print('\nOpciones:')
        print('1.- Escribir')
        print('2.- Leer desde archivo')
        print('3.- Cancelar')
        
        option = select_option('\nSelecciona una opción:', range(1, 4))
        if (option != 3):
            message = ''
            if option == 1:
                message = input('\nIngresa el mensaje:\n')
            elif option == 2:
                message = get_message(input('\nIngresa el nombre del archivo:\n'))
            if message:
                decrypted_message = decrypt(message, encryption_key)
            
                print('\nEl mensaje descifrado es:')
                print(decrypted_message)
                print('------------------------------')
                if confirm_option('\n¿Deseas guardar el resultado?'):
                    filename = input('\nIngresa el nombre del archivo a guardar\n')
                    if (save_message(filename, decrypted_message)):
                        print('\n-- Mensaje guardado en archivo ' + filename + '.txt --')
                        wait()
                    else:
                        print('\n[!] No se pudo guardar el archivo [!]')
                        wait()
            else:
                print('\n[!] No se pudo obtener el mensaje [!]')
                wait()
        else:
            print('\n-- Acción cancelada --')
            wait()
    elif option == 3:
        print('\nGENERAR LLAVE DE CIFRADO')
        if (confirm_option('\n¿Deseas generar una nueva llave de cifrado?, esta reemplazará a la llave actual')):
            encryption_key = generateKey()
            print('\n-- Llave de cifrado generada --')
            wait()
        else:
            print('\n-- Acción cancelada --')
            wait()
    elif option == 4:
        print('\nIMPORTAR LLAVE DE CIFRADO')
        if (confirm_option('\n¿Deseas importar una llave de cifrado?, esta reemplazará a la llave actual')):
            key = get_encryption_key(input('\nIngresa el nombre del archivo:\n'))
            if key:
                encryption_key = key
                print('\n-- Llave de cifrado importada --')
                wait()
            else:
                print('\n[!] No se pudo obtener la llave de cifrado [!]')
                wait()
        else:
            print('\n-- Acción cancelada --')
            wait()
    elif option == 5:
        print('\nEXPORTAR LLAVE DE CIFRADO')
        filename = input('\nIngresa el nombre del archivo a guardar\n')
        if (save_encryption_key(filename, encryption_key)):
            print('\n-- Llave de cifrado guardada en archivo ' + filename + '.key --')
            wait()
        else:
            print('\n[!] No se pudo guardar el archivo [!]')
            wait()
        print()
    elif option == 6:
        print('\nSALIR')
        if (confirm_option('\n¿Deseas salir del sistema?')):
            want_exit = True
            print('\nBye :)')
        else:
            print('\n-- Acción cancelada --')
            wait()
