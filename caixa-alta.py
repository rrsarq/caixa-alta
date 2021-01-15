# Descrição: Modificar texto para maiúscula/minúscula
# Autor: rrs.arq

# Definição das variáveis para o loop do programa

opcao = 0

# Função de limpar

from os import system, name
def clear():
    if name == "nt":
        _ = system("cls")

# Definição das funções maiúsculo e minúsculo

def maiusculo(texto):
    texto=input("Cole aqui texto para deixar em maiúsculo: ")
    caps = texto.upper()
    print()
    print("Selecione e copie o texto modificado:")
    print(caps)
    print()
   
def minusculo(texto):
    texto=input("Cole aqui texto para deixar em minúsculo: ")
    small = texto.lower()
    print()
    print("Selecione e copie o texto modificado:")
    print(small)
    print()

# Rotina de saída

def saida():          
    sair = input("Digite S para sair, L para limpar ou qualquer outra para continuar: ")
    sair = sair.lower()
    if sair == "s":
        exit()
    elif sair == "l":
        clear()
    else:
        print("---")
        

# Loop principal    

while opcao == 0:
        opcao=input("Escolha 1-MAIUSCULO ou 2-minusculo: ") 
        if opcao == str(1):
            print("OK! Tecle Enter:")
            maiusculo(input())
            saida()
            opcao = 0
        elif opcao == str(2):
            print("OK! Tecle Enter:")
            minusculo(input())
            saida()
            opcao = 0
        else:
            print("ERRO! Escolha apenas 1 ou 2")
            print()
            opcao = 0