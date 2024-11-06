inicial = 10
quantidade = 3
soma = 0
while quantidade != 0:
    if inicial  % 2 == 1 :
        soma = soma + inicial
        quantidade = quantidade - 1
    inicial = inicial + 1   
print("soma:", soma)
