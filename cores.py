#Cores no Terminal 
# Sempre que quiser uma cor começa com ( \033[ style text back m)
#                                        \033[0:33:44m]


#            STYLE 
# 0 > None 
# 1 > negrito
# 4 > sublinhado
# 5 > negative = ao inverso 

#            TEXT
# 30 > Branco 
# 31 > Vermelho 
# 32> verde
# 33 > Amarelo 
# 34 > Azul 
# 35 > Rosa
# 36 > Azul cor de água 
# 37 > Cinza 

#            Back 
# 40 em diante até 47 seguindo o padrão de cor de text 
print ('\033[34m'+'Isto eh azul'+'\033[0;0m')
print('\033[46m' +'Isto eh ciano'+'\033[0;0m')
print ('\033[42m'+'\033[1m'+'\033[33m'+'Isto eh amarelo negrito com fundo verde'+'\033[0;0m')
"""
você pode fazer assim para comentar também, linhas grandes etc...
""" 