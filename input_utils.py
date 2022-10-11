# UTILIDADES DE SELECCIÓN DE OPCIONES
# Autor: Ricardo Cárdenas Guevara
# Fecha de creación: 10/10/2022

from time import sleep

def select_option(message, options):
    message += '\n'
    option = input(message)
    while (not option.isdigit() or not int(option) in options):
        print('\n[!] Opción inexistente [!]')
        wait()
        option = input(message)
    return int(option)

def confirm_option(message):
    message += ' [S/N]\n'
    option = input(message).upper()
    while (not option in ['S', 'N']):
        print('\n[!] Opción inexistente [!]')
        wait()
        option = input(message).upper()
    return option == 'S'

def wait():
    sleep(1)