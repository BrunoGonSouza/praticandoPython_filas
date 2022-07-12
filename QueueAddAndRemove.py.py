'''Universidade Cruzeiro do sul
   Bruno gonçalves de souza
   10.05.2022
   Exercicio 06 - Modifique o programa da questão 05 para
   trabalhar com duas filas. Para facilitar seu trabalho, considere
   o comando A para atendimento da fila 1; e B, para atendimento da
   fila 2. O mesmo para chegada de clientes: F para fila 1; e G, para fila 2.'''


senhaF = 1
senhaG = 1
filaF = []
filaG = []

while(True):
    print("--------------------------------------------")
    print("         POUPATEMPO - GUARULHOS")
    print("--------------------------------------------")
    print("F - retirar senha normal")
    print("G - retirar senha preferencial") 
    print("A - chamar senha da fila 1")
    print("B - chamar senha da fila 2")
    print("                                            ")
    
    comando = input("Digite o comando desejado: ")
          
    #Retirar senha:
    
    if (comando == "F" or comando == "f"):

        print(f"Sua senha é: {senhaF}")
        filaF.append(senhaF)
        print(f"Fila Atual (normal): {filaF}")
        senhaF = senhaF + 1

        qtdSenha1 = len(filaF)
        print(f"Pessoas na fila (normal): {qtdSenha1}")
        
    if (comando == "G" or comando == "g"):

        print(f"Sua senha é: {senhaG}")
        filaG.append(senhaG)
        print(f"Fila Atual (preferencial): {filaG}")
        senhaG = senhaG + 1

        qtdSenha2 = len(filaG)
        print(f"Pessoas na fila (preferencial): {qtdSenha2}")    


    #Chamar senha:
    
    if (comando == "A" or comando == "a"):
        if (len(filaF) == 0):
            print("Fila vazia")
        print(f"Din Don - senha {filaF[0]}")
        filaF.pop(0)
        print(f"Fila Atual (normal): {filaF}")
        qtdSenha1 = len(filaF)
        print(f"Pessoas na fila (normal): {qtdSenha1}")

    if (comando == "B" or comando == "b"):
        if (len(filaG) == 0):
            print("Fila vazia")
        print(f"Din Don - senha {filaG[0]}")
        filaG.pop(0)
        print(f"Fila Atual (preferencial): {filaG}")
        qtdSenha2 = len(filaG)
        print(f"Pessoas na fila (preferencial): {qtdSenha2}")

        
          










