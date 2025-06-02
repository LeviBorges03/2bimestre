
pacotes = (
    ("ABC123", "Enviado"),
    ("XYZ789", "Recebido"),
    ("DEF456", "Em transito"),
    ("JKL321", "Enviado"),
    ("MNO654", "Recebido"),
    ("PQR987", "Em transito"),
    ("STU741", "Enviado")
)

#contar quantos pacotes estao em cada status

qtd_enviado = 0
qtd_recebido = 0
qtd_transito = 0


for cod, stat in pacotes:
    if stat == "Enviado":
        qtd_enviado = qtd_enviado + 1
    if stat == "Recebido":
        qtd_recebido = qtd_recebido + 1
    if stat == "Em transito":
        qtd_transito = qtd_transito + 1

# mostrando os resultados das contagens
print("quantidade de pacotes em")
print("Enviado:", qtd_enviado)
print("Recebido:", qtd_recebido)
print("Em transito:", qtd_transito)
print()

#codigo dos pacotes em transito
print("pacotes em transito")
for cod, stat in pacotes:
    if stat == "Em transito":
        print(cod)
print()

# função
def busca_status(codigo):
    # Percorre todos os pacotes
    for cod, stat in pacotes:
        if cod == codigo:
            return stat
    # Se nao encontrou retorna msg
    return "Pacote nao cadastrado"

#  Testando a funcao com exemplos
print("#--- TESTE BUSCA_STATUS ---")
print("STATUS ABC123:", busca_status("ABC123"))  # Deve retornar "Enviado"
print("STATUS PQR987:", busca_status("PQR987"))  # Deve retornar "Em transito"
print("STATUS XXX000:", busca_status("XXX000"))  # Deve retornar "Pacote nao cadastrado"
print()


pacotes_lista = list(pacotes)  # transforma a tupla em lista

#Usando sorted para pegar a lista ordenada pelo codigo
pacotes_ordenados = sorted(pacotes_lista)  # ordena pelo primeiro elemento (codigo)

#Mostrando a tabela ordenada
print("#--- TABELA DE PACOTES ORDENADA POR COD ---")
print("COD\tSTATUS")
for cod, stat in pacotes_ordenados:
    print(cod + "\t" + stat)