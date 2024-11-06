#for w in range(0, 3):
 #   print(w)
import os
os.system('cls')
'''numero=15

if numero % 2 == 0:
    resultado = "Par"
elif numero % 3 == 0:
    resultado = "Multiplo de 3 "  
else:
    resultado = "impar"    
    print(f" O numero{numero} é {resultado}.")   
''' 
'''
idade = 25
salario = 3000

if idade>= 18 and salario >= 2500:
    resultado = "Elegivel para empréstimo."
elif idade >= 18:
    resultado = "Elegivel para empréstimo com consignário." 
else:
    resultado = "Não é elégivel para empréstimo"
print(resultado)

'''
'''
idade=30
salario = 2000

if idade >= 18 and salario >= 3000:
    resultado = "Elegivel para empréstimo."
elif idade >= 18:
    resultado = "Elegivel para empréstimo com um co-signatário"
else:
    resultado = "Não elegovel para empréstimo"
print(resultado)    
'''
'''
idade = 25
tem_cartao = True

if idade >= 18 and tem_cartao == True:
    print ("Você pode comprar o produto.")
else:
    print('Desculpe, você não pode comprar o produto')

'''

'''
nota = 75

if nota > 90 and nota < 80 :
    print("Excelente desempenho")
elif nota >= 80 and nota < 90 :
    print ("Bom desempenho")
elif nota >= 70 and nota < 80:
    print('Desempenho Razoável')
else:
    print('Desempenho Insatisfatório')
'''
'''

5555555555555555555

idade = 22
valor_carrinho = 450
desconto = 0

if idade >= 18 and valor_carrinho >= 500:
    desconto = 15
elif idade < 18 and valor_carrinho >= 300:
    desconto = 10
elif idade < 18 and valor_carrinho < 300:
    desconto = 0
elif idade >= 18 and valor_carrinho < 500 :
    desconto = 5

'''
'''
tem_carteira = True
idade =19
tem_convite = False

if(tem_carteira or idade >=18) and not tem_convite:
    print('Você pode entrar na festa.')
else:
    print("Desculpe, você não pode entrar na festa") 
 
'''
'''
idade = 20
tem_carteira = True
tem_convite = False

if (idade >=18 and tem_carteira) or (tem_convite == True):
    print("Você pode entrar na festa")
else: 
    print("Desculpe, ocorreu um erro.")
'''

''' 777777777777777777777777777

dados= [['maria'18], ['carlos'16],['alex'17]['Sandra'15]]
for i in dados:
    print(i[-1])
'''
''''
print(type)('cao', 'gato', 'elefante','cobra','vespa')

frutas=['morango', 'abacaxi','banana', 'coco']
print(type(frutas))
'''

"""L =[1]
while len(L) < 6:
    L.append(L[-1]*len(L))
    print('soma:',L)"""


'''' xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


inicial = 10
quantidade =3
soma = 0

while quantidade !=0:
    if inicial %2 ==1:
      soma= soma + inicial
      quantidade = quantidade -1
    inicial = inicial + 1
print('Soma', soma)

'''

'''L=[10,12,14,16]
for k in range(3,-5,-1):
    print(L[k])
    '''
''''
#frutas = ['banana', 'laranja','manga', 'uva'] 
#for k in range (-1,-4,-2):
 #   print(frutas[k])


'''
''''
a = ['UF'] + ['RN']
print(len(a))
b= ['4']*4
print(len(b))

'''
'''
total = 0
i = 1
while i <= 5:
    for j in range(3):
        total += i * j
i +=1
print(total)
'''


'''
inicial = 10
quantidade = 3
soma = 0
while quantidade !=0:
    if inicial  % 2 == 1:
        soma = soma + inicial
        quantidade = quantidade - 1
    inicial = inicial + 1   
print("soma:", soma)

'''
'''
contador = 1
while True:
    if contador > 5:
       break
print("Contando", contador + 1)

'''
'''' 
x= []
for i in range(7,1,-1):
    x.append(i)
print(x)'''
'''
linha1 =[1,8.9,2]
linha2=[2,3,4,5]
matriz =[]
matriz.append(linha1)
matriz.append(linha2)
for x in range(0,len(matriz)):
    for y in range (0,len(matriz[x])):
        print(matriz[x][y])
        if (matriz[x][y]) > 5:
            break

'''
'''
#total = 0
#i=1
#while i<= 5:
for j in range(3):
      #  total += i*j
    #i+=1
# print(total)
  #  
'''
'''
L = ['A', 'E', 'I', 'O', 'U']
saida = ""
for k in range(1, -2, -1):
    saida = saida + (L[k+1])
print(saida)
'''
'''linha1 =[1,8,9,2]
linha2=[2,3,4,5]
matriz =[]
matriz.append(linha1)
matriz.append(linha2)
for x in range(0,len(matriz)):
    for y in range (0,len(matriz[x])):
        print(matriz[x][y])
        if (matriz[x][y]) > 5:
            break
'''
'''
a=0
b=7
for i in range(0,2,2):
    a=a+3
    b= b-a
print(a)
print(b)    '''

#b = ['4']*4
#print(len(b))
"""
total=0
i=1
while i<= 5:
    for j in range(3):
        total += i *j
        i +=1
print(total)        
    
"""

"""
def checa_lista(list):
    elem = list[0]
    for a in list:
        if a>elem:
            elem=a
    return elem
    prin(checa_lista([4,4,8,-3]))        
    """
''''
def checa_lista(lst):
    elem = lst[0]
    for a in lst:
        if a > elem:
            elem = a
    return elem

print(checa_lista([4, 4, 8, -3]))
'''

'''
def func():
    x=1
    print(x)
x=10
func()
print(x)    
'''

"""
def funcao_a():
    print("A")

def funcao_b():
    funcao_a()
    print("B")    
print('C')
funcao_a()
funcao_b()
"""

'''a = 20

def funcao_exemplo(x):
    b=10
    resultado = x + a + b
    return resultado
c = funcao_exemplo(5)
'''

