from os import system
system("cls")

def verificarEntrada(entrada:str) -> bool:

    entrada = entrada.lower()
    valorDeRetorno = False;

    for i in range(len(palavraArray)):

        if (entrada in palavraArray[i]):

            realArray[i] = entrada
            valorDeRetorno = True
    
    return valorDeRetorno
            
def desenhoInicial():
    for i in range(len(palavraArray)):
        realArray.append("_")

def desenharArray():
    
    getString = ""
    print('\n')
    for i in range(len(palavraArray)):

            getString += realArray[i]
        
    print(getString)

def fimPrograma():

    array1 = ""
    array2 = ""

    for i in range(len(palavraArray)):

        array1 += palavraArray[i]
        array2 += realArray[i]
    
    if (array1 == array2):
        print("\nParaben vc conseguiu achar a palavra!")
        print(f"Palavra: {array1}")
        return True

    return False

palavara = "carro"
realArray = []
palavraArray = palavara
tentivas = 12
verificador = False

if __name__ == '__main__':

    desenhoInicial()
    while (tentivas > 0):
    
        desenharArray()
        print(f"Tentativas: {tentivas}")
        entradaPalavra = input("Digite uma letra: ")
        
        verificador = verificarEntrada(entradaPalavra)

        if (verificador):
            print("Boa essa letra existe na palavra!")

        else:
            print("Que pena essa letra nao existe na palavra")
            tentivas -= 1
        
        if (fimPrograma()):
            tentivas = 0
