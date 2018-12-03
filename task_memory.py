import random
from function_task_memory import *

memoria = [" "] * 100
opcao = 0
tamanho = 0
letra = ""
resultado = bool

# Pré-define os espaço alocados e não alocados da memória
for i in range(100):
    if(random.randint(0,11) >= 5):
        memoria[i] = "x"
    else:
        memoria[i] = " "

# Chama a função mostrarMemoria
mostrarMemoria(memoria)

while(opcao != 4):
    #Menu do programa
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero")
    opcao = int(input())
    
    # Caso a opcao informada seja 4, a estrutura de repetição deve ser encerrada
    if (opcao == 4):
        print("Saindo do programa...")
        break

    print("Digite o tamanho da informacao")
    tamanho = int(input())
    print("Digite a letra a ser utiliada")
    letra = input()

    # Chama a função inserirLocacao, passado o valor da variável de memoria, opcao, tamanho, letra como parametro para função
    resultado = inserirLocacao(memoria, opcao, tamanho, letra)

    # Informa ser foi ou não alocado na memória
    print(resultado)
    input("Press ENTER to continue...")
    print('\n')

    # Chama a função mostrarMemoria
    mostrarMemoria(memoria)
