import random

memoria = [' '] * 100
opcao = 0
tamanho = 0
letra = ''
tamanhoBuraco = 0
tamanhoBuracoAntigo = 0
lugares = [] * 0
possiveisLugares = [] * 0
proximo = False

for i in range(100):
    if(random.randint(0,11) >= 5):
        memoria[i] = 'x'
    else:
        memoria[i] = ' '
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
while(opcao != 4):
    #Menu do programa
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero")
    opcao = int(input())
    if (opcao == 4):
        break

    print("Digite o tamanho da informacao")
    tamanho = int(input())
    print("Digite a letra a ser utiliada")
    letra = input()

    if(opcao == 1):
        #Implemente aqui a lógica da primeira escolha
        i=0
        while(i<100):
            if memoria[i] == ' ':
                tamanhoBuraco = tamanhoBuraco + 1;
                possiveisLugares.append(i)
                if tamanhoBuraco == tamanho:
                    if len(possiveisLugares) > 0:
                        for j in range(len(possiveisLugares)):
                            memoria[possiveisLugares[j]] = letra
                        proximo = True
            else:
                tamanhoBuraco = 0
                possiveisLugares = [] * 0
                if proximo:
                    proximo = False
                    break
            i = i + 1
    else:
        if (opcao == 2):
            i = 0
            while (i < 100):
                if memoria[i] == ' ':
                    tamanhoBuraco = tamanhoBuraco + 1;
                    possiveisLugares.append(i)
                    if tamanhoBuraco == tamanho and  memoria[i + 1] != ' ':
                        if len(possiveisLugares) > 0:
                            for j in range(len(possiveisLugares)):
                                memoria[possiveisLugares[j]] = letra
                            proximo = True
                else:
                    tamanhoBuraco = 0
                    possiveisLugares = [] * 0
                    if proximo:
                        proximo = False
                        break
                i = i + 1
        else:
            if(opcao == 3):
                #Implemente aqui a lógica da pior escolha
                i = 0
                while (i < 100):
                    if memoria[i] == ' ':
                        tamanhoBuraco = tamanhoBuraco + 1;
                        possiveisLugares.append(i)
                        if tamanhoBuraco >= tamanho:
                            if tamanhoBuracoAntigo == 0:
                                tamanhoBuracoAntigo = len(possiveisLugares)
                            else:
                                if tamanhoBuracoAntigo < len(possiveisLugares):
                                    tamanhoBuracoAntigo = len(possiveisLugares)
                                    lugares = possiveisLugares
                    else:
                        tamanhoBuraco = 0
                        possiveisLugares = [] * 0
                    i = i + 1
                
                if len(lugares) != 0:
                    for i in range(tamanho):
                        memoria[lugares[i]] = letra
                
                tamanhoBuracoAntigo = 0
                lugares = [] * 0

    # Aqui você deve imprimir todo o conteúdo da variável memória
    for i in range(0, 20):
        print(memoria[i], end="|")
    print()
    for i in range(20, 40):
        print(memoria[i], end="|")
    print()
    for i in range(40, 60):
        print(memoria[i], end="|")
    print()
    for i in range(60, 80):
        print(memoria[i], end="|")
    print()
    for i in range(80, 100):
        print(memoria[i], end="|")
    print()
