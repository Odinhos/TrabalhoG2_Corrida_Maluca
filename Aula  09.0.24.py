import os, time
os.system('cls')

usuario = input ('Usuarios:')
senha  = input('Senha:')

if usuario == "Donald" and senha == 'Trump':
   
    print('Acesso Autorizado!')
    time.sleep(3)
    os.system('cls')
else:
    print ('Usuario ou Senha incorretos!')
    quit()

print ('########### Código de Ativação - 4756345')  