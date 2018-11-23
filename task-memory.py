import random

memoria = [" "] * 100
opcao = 0
tamanho = 0
letra = ""
resultado = bool

# Função que imprimi o estado atual da memória
def mostrarMemoria():
    for i in range(0,20):
        print(memoria[i], end="|")
    print()
    for i in range(20,40):
        print(memoria[i], end="|")
    print()
    for i in range(40,60):
        print(memoria[i], end="|")
    print()
    for i in range(60,80):
        print(memoria[i], end="|")
    print()
    for i in range(80,100):
        print(memoria[i], end="|")
    print()

# Função que realiza todo raciocínio para a alocação da memória conforme a opção desejada
def inserirLocacao(opcao):

    # Variáveis da função
    tamanhoBuraco = 0
    tamanhoBuracoAntigo = 0
    lugares = [] * 0
    possiveisLugares = [] * 0
    memoriaAntiga = memoria[:]
    proximo = False
    mensagem = ""

    i=0
    while(i<100):
        if memoria[i] == " ":
            # Armazena a quantidade de lugares vazios
            tamanhoBuraco = tamanhoBuraco + 1
            # Armazena no final da lista o local do lugar vazio
            possiveisLugares.append(i)
            # Se a opcao for igual a 1 ou a 2 e seguir as expressões lógicas fazer esse bloco de código
            if (tamanhoBuraco == tamanho and opcao == 1) or (tamanhoBuraco == tamanho and  memoria[i + 1] != " " and opcao == 2):
                if len(possiveisLugares) > 0:
                    # Repete a estrutura conforme a quantidade de lugares
                    for j in range(len(possiveisLugares)):
                        # Atribui a letra nos endereços vazios
                        memoria[possiveisLugares[j]] = letra
                    proximo = True
            # Se a opcao for igual a 3 e seguir a expressão lógica fazer esse bloco de código
            if tamanhoBuraco >= tamanho and opcao == 3:
                # Pegar o primeiro lugar possíveis 
                if tamanhoBuracoAntigo == 0:
                    tamanhoBuracoAntigo = len(possiveisLugares)
                else:
                    # Pegar o maior lugar possível
                    if tamanhoBuracoAntigo < len(possiveisLugares):
                        tamanhoBuracoAntigo = len(possiveisLugares)
                        lugares = possiveisLugares
        else:
            # Limpando dados das variavéis
            tamanhoBuraco = 0
            possiveisLugares = [] * 0
            # Se a variável for verdadeira para a estrura de retição WHILE
            if proximo:
                proximo = False
                break
        i = i + 1

    # Se a opcao for igual a 3
    if opcao == 3:
        # Conferindo se existe lugares para se alocar
        if len(lugares) != 0:
            # Alocando valores na memória
            for i in range(tamanho):
                memoria[lugares[i]] = letra
        # Limpando dados das variavéis
        tamanhoBuracoAntigo = 0
        lugares = [] * 0

    # Verifica se os dados foram alocados na memória e atribui uma mensagem à variavél mensagem
    if memoriaAntiga == memoria:
        mensagem = "\n Information of the memory: Impossible allocate \n"
    else:
        mensagem = "\n Information of the memory: Allocated with success! \n"

    # Retorna a variável mensagem para quem chamar essa função 
    return mensagem

# Pré-define os espaço alocados e não alocados da memória
for i in range(100):
    if(random.randint(0,11) >= 5):
        memoria[i] = "x"
    else:
        memoria[i] = " "

# Chama a função mostrarMemoria
mostrarMemoria()

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

    if(opcao == 1):
        # Chama a função inserirLocacao, passado o valor da variável opcao como parametro para função
        resultado = inserirLocacao(opcao)

    if (opcao == 2):
        # Chama a função inserirLocacao, passado o valor da variável opcao como parametro para função
        resultado = inserirLocacao(opcao)

    if(opcao == 3):
        # Chama a função inserirLocacao, passado o valor da variável opcao como parametro para função
        resultado = inserirLocacao(opcao)

    # Informa ser foi ou não alocado na memória
    print(resultado)

    # Chama a função mostrarMemoria
    mostrarMemoria()
