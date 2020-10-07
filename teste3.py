import os
os.system('clear')

tam_max = 26

def Mod():
    while True:
        print('.'*30)
        print('Sistema de acesso a área contaminada ')
        mode = input('''Encriptar ou Descriptar?
        [E] Encriptar        [D] Descriptar\n-: ''')

        if mode in 'Encriptar Descriptar D E d e'.split():
            return mode
        else:
            pass

def Key():
    key = 0

    while True:
        key = int(input('Entre com um número de chave (1-26):'))

        if 1 <= key <= 26:
            return key

def msgTranslate(mode, msg, key):
    if mode[0] == 'd' or mode[0] == 'D':
        key *= -1
    translate = ''

    for symbol in msg:
        if symbol.isalpha():
            num = ord(symbol)
            num += key 

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26

            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translate += chr(num)
        else:
            translate += symbol
    return translate

def Main():
    mode = Mod()
    msg = input('Entre com o aceso: ')
    security = str(input('Os equipamentos de segurança estão ok ?[S/N]'))
    key = Key()

    print('Tradução do seu acesso :')
    print(msgTranslate(mode, msg, key))

init = Main()

# alterando