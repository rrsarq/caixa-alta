# Definição das variáveis para o loop do programa
repetir = 1
opcao = 0

# Definição das funções maiúsculo e minúsculo 

def maiusculo(texto):
    texto=input("Cole aqui texto para deixar em maiúsculo: ")
    caps = texto.upper()
    print("")
    print("Selecione e copie o texto modificado:")
    print(caps)
    print("")
   
def minusculo(texto):
    texto=input("Cole aqui texto para deixar em minúsculo: ")
    small = texto.lower()
    print("")
    print("Selecione e copie o texto modificado:")
    print(small)
    print("")
    

while repetir == 1:
    while opcao == 0:
        opcao=input("Escolha 1-MAIUSCULO ou 2-minusculo: ") 
        if opcao == str(1):
            print("OK! Tecle Enter:")
            maiusculo(input())
            sair = input("Digite S para sair ou qualquer outra para continuar: ")
            if sair == "S":
                repetir = 0
                exit()
            else:
                opcao = 0
                print("---")
        if opcao == str(2):
             print("OK! Tecle Enter:")
             minusculo(input())
             sair = input("Digite S para sair ou qualquer outra para continuar: ")
             if sair == "S":
                repetir = 0
                exit()
             else:
                opcao = 0
                print("---")
        else:
             opcao = 0