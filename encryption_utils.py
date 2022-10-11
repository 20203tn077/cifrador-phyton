# UTILIDADES DE CIFRADO
# Autor: Ricardo Cárdenas Guevara
# Fecha de creación: 10/10/2022

import random
from properties import ALPHABET

def generateKey():
    key = [*ALPHABET]
    random.shuffle(key)
    return ''.join(key)

def encrypt(message, key):
    result = ''
    for char in message:
        for i in range(len(ALPHABET)):
            if char == ALPHABET[i]:
                result += key[i]
                break
        else:
            result += char
    return result

def decrypt(message, key):
    result = ''
    for char in message:
        for i in range(len(ALPHABET)):
            if char == key[i]:
                result += ALPHABET[i]
                break
        else:
            result += char
    return result
