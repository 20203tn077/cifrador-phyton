# ARCHIVO PRINCIPAL
# Autor: Ricardo Cárdenas Guevara
# Fecha de creación: 10/10/2022

from encryption_utils import *
from file_utils import *
from input_utils import *

encryption_key = generateKey()
want_exit = False

# Menú principal
# Se sigue mostrando hasta que se elija la opción de salir
while not want_exit:
    print('\n====================================')
    print('>> SISTEMA DE CIFRADO DE MENSAJES <<')
    print('====================================')
    print('Llave de cifrado: [' + encryption_key.replace('\n', '')[:13] + '...]')
    print('\nOpciones:')
    print('1.- Cifrar mensaje')
    print('2.- Descifrar mensaje')
    print('3.- Generar llave de cifrado')
    print('4.- Importar llave de cifrado')
    print('5.- Exportar llave de cifrado')
    print('6.- Salir')
    option = select_option('\nSelecciona una opción:', range(1, 7))
    if option == 1:
        # Submenú opción de cifrar mensaje
        print('\nCIFRAR MENSAJE')
        print('\nOpciones:')
        print('1.- Escribir')
        print('2.- Leer desde archivo')
        print('3.- Cancelar')
        option = select_option('\nSelecciona una opción:', range(1, 4))
        if (option != 3):
            message = ''
            # Se obtiene el mensaje de la fuente correspondiente a la opción seleccionada
            if option == 1:
                message = input('\nIngresa el mensaje:\n')
            elif option == 2:
                message = get_message(input('\nIngresa el nombre del archivo:\n'))
            # Se evalúa en caso de no exista o no se haya podido obtener el mensaje
            if message:
                # Cifrado del mensaje
                encrypted_message = encrypt(message, encryption_key)
                print('\nEl mensaje cifrado es:\n' + encrypted_message + '\n------------------------------------')
                if confirm_option('\n¿Deseas guardar el resultado?'):
                    # Guardado del resultado en archivo de texto
                    filename = input('\nIngresa el nombre del archivo a guardar\n')
                    if (save_message(filename, encrypted_message)):
                        alert('Mensaje guardado en archivo ' + filename + '.txt')
                    else:
                        warning('No se pudo guardar el archivo')
            else:
                warning('No se pudo obtener el mensaje')
        else:
            alert('Acción cancelada')
    elif option == 2:
        # Submenú opción de descifrar mensaje
        print('\nDESCIFRAR MENSAJE')
        print('\nOpciones:')
        print('1.- Escribir')
        print('2.- Leer desde archivo')
        print('3.- Cancelar')
        option = select_option('\nSelecciona una opción:', range(1, 4))
        if (option != 3):
            message = ''
            # Se obtiene el mensaje de la fuente correspondiente a la opción seleccionada
            if option == 1:
                message = input('\nIngresa el mensaje:\n')
            elif option == 2:
                message = get_message(input('\nIngresa el nombre del archivo:\n'))
            # Se evalúa en caso de no exista o no se haya podido obtener el mensaje
            if message:
                # Descifrado del mensaje
                decrypted_message = decrypt(message, encryption_key)
                print('\nEl mensaje descifrado es:')
                print(decrypted_message)
                print('------------------------------')
                if confirm_option('\n¿Deseas guardar el resultado?'):
                    # Guardado del resultado en archivo de texto
                    filename = input('\nIngresa el nombre del archivo a guardar\n')
                    if (save_message(filename, decrypted_message)):
                        alert('Mensaje guardado en archivo ' + filename + '.txt')
                    else:
                        warning('No se pudo guardar el archivo')
            else:
                warning('No se pudo obtener el mensaje')
        else:
            alert('Acción cancelada')
    elif option == 3:
        print('\nGENERAR LLAVE DE CIFRADO')
        if (confirm_option('\n¿Deseas generar una nueva llave de cifrado?, esta reemplazará a la llave actual')):
            # Generación de nueva llave de cifrado
            encryption_key = generateKey()
            alert('Llave de cifrado generada')
        else:
            alert('Acción cancelada')
    elif option == 4:
        print('\nIMPORTAR LLAVE DE CIFRADO')
        if (confirm_option('\n¿Deseas importar una llave de cifrado?, esta reemplazará a la llave actual')):
            # Importación de llave de cifrado desde archivo
            # Se evalúa antes de reemplazar la clave en caso de que haya fallado la lectura del archivo
            key = get_encryption_key(input('\nIngresa el nombre del archivo:\n'))
            if key:
                encryption_key = key
                alert('Llave de cifrado importada')
            else:
                warning('No se pudo obtener la llave de cifrado')
        else:
            alert('Acción cancelada')
    elif option == 5:
        print('\nEXPORTAR LLAVE DE CIFRADO')
        # Guardado de llave de cifrado en archivo KEY
        filename = input('\nIngresa el nombre del archivo a guardar\n')
        if (save_encryption_key(filename, encryption_key)):
            alert('Llave de cifrado guardada en archivo ' + filename + '.key')
        else:
            warning('No se pudo guardar el archivo')
        print()
    elif option == 6:
        print('\nSALIR')
        if (confirm_option('\n¿Deseas salir del sistema?')):
            want_exit = True
            print('\nBye :)')
        else:
            alert('Acción cancelada')
