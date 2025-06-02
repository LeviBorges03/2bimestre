numero = (5, 8, 12, 8, 7, 8, 3)
# para ser uma tupla precisa estar entre parenteses

print("tupla original:", numero)
# imprimindo para o usuario

print("Tamanho da tupla", len(numero))

print("acessando indice", numero[2])

print("fazendo um slice do 2 ao 5", numero[2:5])
# o slicing nao pega o ultimo numero do recorte

print("quantas vezes o numero 8 repete;", numero.count(8))
# saber qunats vezes um numero repete

print("posição da primeira ocorrencia do numero 7:", numero.index(7))

# min minimo max maximo sum soma

minimo_tupla = min(numero)
# recebe minimo

maximo_tupla = max(numero)
# recebe maximo

soma_tupla = sum(numero)
# recebe soma
print("soma da tupla:", soma_tupla)

ordenada_tupla = sorted(numero)
# recebe tupla ordenada
print("ordenada tupla:", ordenada_tupla)

print("se algum numero está na tupla:", 4 in numero)
# devolve verdeiro ou falso

numero2 = (15, 20)
tupla_concatenada = numero+numero2
print("a concatenação das tuplas 1 e a 2 resultam na tupla:", tupla_concatenada)

tupla_DUPLICADA= numero*2 
print("multiplicação",tupla_DUPLICADA)
# NEM A SOMA E NEM A MULTIPLICAÇÃO FUNCIOANM NAS TUPLAS.