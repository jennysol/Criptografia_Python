from time import sleep

print('\033[34m'+'APS 2020/2 - Criptografia / Descriptografia'+'\033[0;1m')

print('-')
print('-')

print('Um navio foi aprendido pela guarda costeira brasileira \npor transportar lixo tóxico da Ásia para a região norte do Brasil.\n')
print('\033[33m'+'Somente inspetores devidamente trajados com roupas especiais poderão adentrar no navio ! \n'+'\033[0;0m')
print('Por razões legislativas o navio deve permanecer a uma distancia segura de: 50 quilômetros da costa \ne todo e qualquer contato deverá ser realizado por meio de \nhelicópteros, para minimizar e restringir o contato.\n')

print('Segue o questionário a respeito da entrada do navio: \n')
print('Não nos responsabilizamos por suas atitudes !\n')
print('Favor, responder apenas os inspetores.\n')

# Entrada de dados
nome = str(input('Digite seu nome: '))

result = ''
banco = []

print('-')
print('-')

print('Digite sua senha de inspetor, caso não tenha uma digite N.\n')

while True:
    insp = str(input('Digite sua senha: ')).upper()

    if insp != banco and insp != 'N':
        print('\033[31m'+'ERRO! Senha incorreta'+'\033[1;0m')

    elif insp != banco:
        break

if insp == 'N':
    senha = input('\nCrie sua senha: ')
    x = senha.upper()

    print('\033[34m'+'\nAgora iremos criptografar sua senha para torna-la mais segura ...\n'+'\033[0;0m')
    sleep(1)

    seg = input('Digite uma palavra aleatória como chave de segurança: ')
    banc = 'ABCDEFGHIJKLMNOPQR@#$%*¨&STUVWXYZ1234567890'
    txt = senha.upper()

    for i in txt:
        if i in banc:
            posi = banc.find(i)
            posi = (posi + len(seg)) % 36
            result = result + banc[posi]
            banco = result                   

inicio = input('\nTem certeza que deseja entrar no navio?').upper()

if inicio == 'S':
    roupa = str(input('\nVocê está com todos os equipamentos de segurança necessários? ')).upper()
    if roupa == 'S':
        heli = str(input('\nCerto, o helicoptero te espera, deseja entrar?')).upper()
        if heli == 'S':
            print('\033[32m'+'\n' + nome + ' você entrou no navio. \n'+'\033[0;0m')
            print(f'( Sua nova senha criptografada passou de {senha} para {result} )')
        if heli != 'S':
            print("\n Adeus!")  
    else:
        print("\n Adeus!")    
else:
    print("\n Adeus!")

descriptografar = input("\nDeseja descriptografar sua senha [S/N]?\n").upper()
if descriptografar == 'S':
    print('\033[34m'+'\nDescriptografando ...\n'+'\033[0;0m')
    sleep(1)
    print(f"Sua senha descriptografada {senha}")
else:
    print("\n Adeus!")
