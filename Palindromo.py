# -*- coding: utf-8 -*-

def palindrome(word):
    reverse_letters = []

    for letter in word:
        reverse_letters.insert(0, letter)
    reversed_word = ''.join(reverse_letters)

    if reversed_word == word:
        return True
    return False

def palindrome2(word):
    reversed_word = word[::-1]

    if reversed_word == word:
        return True
    return False

if __name__ == '__main__':
    word = str(input('Escribe una palabra: '))

    result = palindrome2(word)

    if result is True:
        print('{} sí es un palíndromo'.format(word))
    else:
        print('{} no es un palíndromo'.format(word)) 
# ----------------------------------- Nota ----------------------------------- #
# Insert sirve para insertar los datos en la variable a partir de la posicion 0
# Join sirve para ingresar datos ya establecidos

