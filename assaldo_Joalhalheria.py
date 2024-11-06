import os
os.system('cls')
import pyttsx3
print ("Responda as perguntas a seguir, Reponda 0 para NÂO, e 1 para SIM")
telefonou = input ('Telefonou para a vitima:')
telefonou = int(telefonou)
local = input ('Esteve no local do Crime:')
local = int(local)
mora = input (' Mora perto da vítima:')
mora = int(mora)
devia = input (' Devia para vitima:')
devia = int(devia)
trabalhou = input (' Já trabalhou com a vitima:')
trabalhou = int(trabalhou)
participacaoCrime = telefonou + local + mora + devia + trabalhou
if participacaoCrime  < 2 :
    print ('Inocente')
elif participacaoCrime == 2 :
    print ('Suspeito')
elif participacaoCrime <=4 :
    print ('Cumplice')
else :
    print('Assaltante')
