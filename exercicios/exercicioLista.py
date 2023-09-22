listaPY = [] #Cria a lista

i = 0

while i != 10: #Laço de repetição para adicionar itens na lista
    addValor = input('Digite o valor a ser adicionado: (Para sair digite um valor negativo)') #Lê o valor inserido pelo usuário
    listaPY.append(addValor)
    i = i + 1

print(listaPY) #Mostra dados da lista
