#Escreva um programa que abra um arquivo digitado pelo usuário e imprima seu conteúdo na tela.   


#codigo para o usuário escrever o arquivo designado
arquivo = input("Digite o nome do arquivo: ")

#variável chamada para abrir o arquivo
arq = open(arquivo, "r")

#loop para pegar todos os caracteres do arquivo designado
for i in arq:
    print(i)

#imprimindo a variável que contem o arquivo
print(arq)

#fechando o arquivo
arq.close()