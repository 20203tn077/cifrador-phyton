# UTILIDADES DEL SISTEMA DE FICHEROS
# Autor: Ricardo Cárdenas Guevara
# Fecha de creación: 10/10/2022

import os
from properties import KEYS_DIR, MESSAGES_DIR

def get_message(name):
    try:
        file = open(os.path.join(MESSAGES_DIR, name + '.txt'))
        return file.read()
    except:
        return
    
def save_message(name, message):
    try:
        file = open(os.path.join(MESSAGES_DIR, name + '.txt'), 'w')
        file.write(message)
        file.close
        return True
    except:
        return False
    
def get_encryption_key(name):
    try:
        file = open(os.path.join(KEYS_DIR, name + '.key'))
        return file.read()
    except:
        return
    
def save_encryption_key(name, key):
    try:
        file = open(os.path.join(KEYS_DIR, name + '.key'), 'w')
        file.write(key)
        file.close
        return True
    except:
        return False