repetir = 0
option = 0

def maiusculo(texto):
    texto=input("Cole aqui texto para deixar em maiúsculo: ")
    caps = texto.upper()
    print(caps)

def minusculo(texto):
    texto=input("Cole aqui texto para deixar em minúsculo: ")
    small = texto.lower()
    print(small)

while repetir == 0:
    while option == 0:
        option=input("Escolha 1-MAIUSCULO 2-minusculo: ") 
        if option == str(1):
            maiusculo(input())
            option = 0
        if option == str(2):
             minusculo(input())
             option = 0
        else:
             option=0