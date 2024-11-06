import os, time,random,pyttsx3
fala  = pyttsx3.init()
os.system('cls')
from colorama import Fore, Back, Style, init
init(autoreset=True)

print(Fore.GREEN +"Boas Vindas....!!? \nO Perigo está Prestes a COMEÇAR...JOGOS MORTAIS!!?")
fala.say("Boas Vindas....!!? \n O Perigo está Prestes a COMEÇAR....JOGOS MORTAIS!!?")
fala.runAndWait()
time.sleep(3)
os.system('cls')

os.system("color 4")
print(Fore.RED + " Que Comece o Jogo !!! " )
fala.say("Que Comece o Jogo!!?")
fala.runAndWait()

ascii_art = """

          _                         __  __            _        _       _ _ 
  ( | )      | |                       |  \/  |          | |      (_)     ( | )
   V V       | | ___   __ _  ___  ___  | \  / | ___  _ __| |_ __ _ _ ___   V V 
         _   | |/ _ \ / _` |/ _ \/ __| | |\/| |/ _ \| '__| __/ _` | / __|      
        | |__| | (_) | (_| | (_) \__ \ | |  | | (_) | |  | || (_ | \__ \      
         \____/ \___/ \__, |\___/|___/ |_|  |_|\___/|_|   \__\__,_|_|___/      
                       __/ |                                                   
                      |___/    

                      
                      Nome: Osvaldo Aguiar dos Santos RA : 1137350
                      """


print(ascii_art)  

random_number = random.randint(1, 3)
print(random_number)      
init(autoreset=True)

fala.say( ' JOGO DA ADIVINHAÇÃO, DIGITE UM NUMERO ENTRE 1, 2 ou 3: ')
fala.runAndWait()
pergunta1 = int(input('JOGO DA ADIVINHAÇÃO, DIGITE UM NUMERO ENTRE 1, 2 ou 3: '))

if pergunta1 == random_number :
   print (Style.BRIGHT + ' VOCÊ CONSEGUI ENTRAR NA FASE 1 !!!')
   fala.say(Style.BRIGHT +' VOCÊ CONSEGUIU ENTRAR NA FASE 1 !!!')
   fala.runAndWait()

else:
  print(Style.BRIGHT + 'TE PEGUEI, VOCÊ TÁ FORA DO JOGO, TENTE OUTRA VEZ !!!? ')
  fala.say('TE PEGUEI, VOCÊ TÁ FORA DO JOGO, TENTE OUTRA VEZ !!!? ')
  fala.runAndWait()
  quit()

  os.system('cls')

 
print ("SEGUNDA FASE : POTENCIA MORTAL")
fala.say("SEGUNDA FASE : POTENCIA MORTAL!")
fala.runAndWait()

numeroAleatorio2 = random.randint(1,9)
numeroAleatorio3 = random.randint(1,9) 

calculo1 = numeroAleatorio2 ** numeroAleatorio3
print(calculo1)

print (numeroAleatorio2, "**", numeroAleatorio3)
fala.say("qual é o resultado da operação acima")
fala.runAndWait()

calc2 = int(input("Qual é a resultado da operação ACIMA!!!!"))
if calc2 == calculo1 :
    print ("RESULTADO CORRETO, PASSOU PARA PROXIMA FASE...ALERTA MÁXIMO!!!?")
    fala.say("RESULTADO CORRETO, PASSOU PARA PROXIMA FASE...ALERTA MÁXIMO!!!?..")
    fala.runAndWait()

else :
    print(Fore.RED + "Você Perdeu...ALERTA MÁXIMO!!!?")
    fala.say("Perdeu Malandro !!?")
    fala.runAndWait()
    quit()
    
os.system("cls")

os.system("cls")

print("CHEGOU O SEU FIM... FORMULA DO DESESPERO")
fala.say("AGORA CHEGA! É O SEU FIMMMMMMM : FORMULA DO DESESPERO!!")
fala.runAndWait()

time.sleep(2)
 
calculo2 = (pergunta1 + calc2) ** pergunta1 - calc2 
print(calculo2)

print("AGORA CALCULE: ((RESPOSTA FASE 01 + RESPOSTA FASE 02) ** RESPOSTA FASE 1 - RESPOTA 02)")
fala.say("soma as duas primeiras resposta, e depois subritraia as duas perimeiras resposta, e por final muiltiplique as duas... ")
fala.runAndWait()
resposta3 = int(input("Qual é a resposta da calculo kkkkkkk :"))
if resposta3 == calculo2 :
    print("VC CONSEGUIU..")
    fala.say("VC CONSEGUIU...")
    fala.runAndWait()
else :
    print(Style.BRIGHT + "Chegou o sem FIM, Diga Tchau")
    fala.say()
    fala.runAndWait()
    
os.system("cls")

###
print("Nessa fase você perde, vamos testar sua memória!!!")
fala.say("vamos ver realmente se vc é ótimo de memoria ")
fala.runAndWait()

num1 = random.randint(1,9)
time.sleep(1)
os.system("cls")
num2 = random.randint (1,9)
time.sleep(1)
os.system("cls") 
num3 = random.randint(1,9) 
time.sleep(1)
os.system("cls") 
num4 = random.randint(1,9) 
time.sleep(1)
os.system("cls")
num5 = random.randint(1,9)
time.sleep(1)
os.system("cls")

sequencia = str(num1)+str(num2)+str(num3)+str(num4)+str(num5)

print(sequencia)
resposta4 = input("Qual é a sequencia dos número mostrado??")

if resposta4 == sequencia :
    print("TÁ LIGADO!! ")
    fala.say("TÁ LIGADO")
    fala.runAndWait()
else :
    print("Você não merece ganhar..já chegou longe...")
    fala.say("Você não merece ganhar..já chegou longe...")
    fala.runAndWait()
    os.system ("cls")
    
    print("Ultimo desafio...")
    fala.say("Quinta fase, realmente você foi muito longe...")
    fala.runAndWait()
    
calculeBits = (((41533440 / 8 )/ 1024) / 1024)
print (calculeBits)



fala.say("Um programador encontra um nano computador que trabalha apenas com bits  O computador tem exatamente 41.533.440 bits de memória. Quantos Megabytes isso representa?")
fala.runAndWait()
resposta5 = float(input(" Um progamador  encontra um nano computador  que trabalha apenas com bits. o computador tem  exatamente 41.533.440 BITS de memoria. quantos megabytes isso representa?"))
if resposta5 == calculeBits :
    print("Felizardo você conseguiu... ")
    fala.say("Parabéns, você está livre...")
    fala.runAndWait()
else :
    print("já tava te aguradando...    seu computador será desliado em 1     2     3 ...")
    fala.say("já tava aguardando..    seu computador será desliado em 1     2     3 ...")
    fala.runAndWait()




 
                      