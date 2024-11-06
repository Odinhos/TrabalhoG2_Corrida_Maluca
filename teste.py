import time, pyttsx3, random, os
fala  = pyttsx3.init()
os.system("cls")

os.system("color 2")

print("vamos jogar!!!")
fala.say("vamos jogar!!!")
fala.runAndWait()

time.sleep(1)

os.system("color 4")

fala.say("seja bem-vindo, aos jogos mortais!: ")
fala.runAndWait()

time.sleep  (2)


print("VAMOS COMEÇAR:...   VAMOS TESTAR SUA SORTE!!!!!!!!!!!!")
fala.say("VAMOS COMEÇAR:...   VAMOS TESTAR SUA SORTE!!!!!!!!!!!!")
fala.runAndWait()

numeroaleatorio = random.randint (1,3)

print(numeroaleatorio)


fala.say("escolha um número aleatorio de (1 2 e 3)")
fala.runAndWait()


respota1 = int(input("ADIVINHE O NUMERO SORTEADO escolha um numero de  1 A 3....: "))
if respota1 == numeroaleatorio :
    print ("VOCÊ TEVE SORTE DESSA VEZ!!!")
    fala.say ("você passou dessa vez, vamos para a proxima!")
    fala.runAndWait()

else:
    print ("VOCÊ PERDEU!!!")
    fala.say ("você errou!")
    fala.runAndWait()
    quit()

os.system("cls")

print ("FASE DOIS: POTENCIA MORTAL")
fala.say("fase dois: potência mortal!")
fala.runAndWait()

numeroAleatorio2 = random.randint(1,9)
numeroAleatorio3 = random.randint(1,9) 

calculo = numeroAleatorio2 ** numeroAleatorio3
print(calculo)

print (numeroAleatorio2, "**", numeroAleatorio3)
fala.say("qual é o resultado da operação acima")
fala.runAndWait()

respota2 = int(input("Qual é a respota da operação ACIMA!!!!"))
if respota2 == calculo :
    print ("RESPOTA CORRETA DA OPERAÇÃO ACIMA?")
    fala.say("Resposta correta! passou para proxíma fase. tenha cuidado..")
    fala.runAndWait()

else :
    print("Você errou!!! é teu fimmm")
    fala.say("hahahhah você errou! é o seu fim")
    fala.runAndWait()
    quit()
    
os.system("cls")

print("AGORA SEU FIM... FORMULA DO DESESPERO")
fala.say("AGORA CHEGA! SEU FIMMM : FORMULA DO DESESPERO!!")
fala.runAndWait()

time.sleep(2)

calculo2 = (respota1 + respota2) ** respota1 - respota2 
print(calculo2)

print("AGORA CALCULE: ((RESPOSTA FASE 01 + RESPOATA FASE 02) ** RESPOSTA FASE 1 - RESPOTA 02)")
fala.say("soma as duas primeiras resposta, e depois subritraia as duas perimeiras resposta, e por final muiltiplique as duas... ")
fala.runAndWait()
resposta3 = int(input("Qual é a resposta da calculo hehheheh :"))
if resposta3 == calculo2 :
    print("foi por pouco...")
    fala.say("foi por pouco...")
    fala.runAndWait()
else :
    print("é o seu fimmm, hahahahah")
    fala.say()
    fala.runAndWait()
    
os.system("cls")

print("Nessa parte você perde, eu vou testar mais uma vez sua memoria!!!")
fala.say("vamos ver realmente se vc é bom de memoria ")
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
    print("TÁ esperto!! ")
    fala.say("tavesperto")
    fala.runAndWait()
else :
    print("Você não merece ter chegado até aqui...")
    fala.say("Você não merece ter chegado até aqui...")
    fala.runAndWait()
    os.system ("cls")
    
    print("Ultimo desafio...")
    fala.say("Quinta fase, realmente você foi muito longe...")
    fala.runAndWait()
    
calculeBits = (((41533440 / 8 )/ 1024) / 1024)
print (calculeBits)



fala.say("Um programador encontra um nano computador que trabalha apenas com bits  O computador tem exatamente 41.533.440 bits de memória. Quantos Megabytes isso representa?")
fala.runAndWait()
resposta5 = float(input("''' Um progamador  encontra um nano computador  que trabalha apenas com bits. o computador tem  exatamente 41.533.440 BITS de memoria. quantos megabytes isso representa?"""))
if resposta5 == calculeBits :
    print("infelizmente você conseguiu... ")
    fala.say("Parabens, você está livre...")
    fala.runAndWait()
else :
    print("já tava te esperando...    seu computador será desliado em 1     2     3 ...")
    fala.say("já tava te esperando...    seu computador será desliado em 1     2     3 ...")
    fala.runAndWait()